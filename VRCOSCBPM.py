import configparser
from os.path import exists
import time
import datetime
import tekore as tk
from pythonosc.udp_client import SimpleUDPClient

# =======================
# Load Configuration

config = configparser.ConfigParser()
config.read('vrcoscbpm.cfg')

IP = str(config['VRCOSCBPM']['IP'])
Port = int(config['VRCOSCBPM']['Port'])
client_id = str(config['VRCOSCBPM']['client_id'])
client_secret = str(config['VRCOSCBPM']['client_secret'])
redirect_uri = str(config['VRCOSCBPM']['redirect_uri'])

AnimationBPM = int(config['VRCOSCBPM']['AnimationBPM'])

# =======================
# Tekore Setup

app_token = tk.request_client_token(client_id, client_secret)

spotify = tk.Spotify(app_token) 

# =======================
# Authorization

TekoreCFG = 'tekore.cfg'

if exists(TekoreCFG) == False:   # Generate User Token
    conf = (client_id, client_secret, redirect_uri)
    token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)
    
    input('Press any button to build tekore.cfg')
    tk.config_to_file(TekoreCFG, conf + (token.refresh_token,))
    input('Built tekore.cfg. Press any button to continue')
    print('\n' * 3)

conf = tk.config_from_file(TekoreCFG, return_refresh=True)
user_token = tk.refresh_user_token(*conf[:2], conf[3])   
    
spotify.token = user_token

# =======================
# Functions

def SendOSC(ip, port, AvatarParamPath, Variable):
    client = SimpleUDPClient(ip, port)  # Create client
    
    client.send_message(AvatarParamPath, Variable)   # Send float message
    
    print('Sent ' + str(Variable) + ' to ' + AvatarParamPath + ' at ' + str(IP) + ':' + str(Port))

def IsPlaying(playback): # Check if 'playback' is a valid track
    if playback is None:
        return False
    return True

def GetTrack(): # Get the User's currently playing Spotify track
    Track = spotify.playback()
    if IsPlaying(Track) is False:
        return False
    return Track.item

def TrackTempo(Track): # Get The tempo of a track
    TrackTempo = spotify.track_audio_features(Track.id).tempo
    return TrackTempo

def DivideBPM(RawBPM): # Turn a Tempo into a fraction of 'AnimationBPM'
    while RawBPM >= AnimationBPM:
        RawBPM /= 2
    
    DividedBPM = RawBPM / AnimationBPM
    
    return DividedBPM

def main():
    while True:
        CurrentTrack = GetTrack()
        
        print(datetime.datetime.now())
        if CurrentTrack is False:
            print('N/a (User Not Playing)')
            SendOSC(IP, Port, "/avatar/parameters/BPM", 0.0)
        else:
            CurrentTrackTempo = TrackTempo(CurrentTrack)
            
            OSCBPM = DivideBPM(CurrentTrackTempo)
            
            print('now playing: ' + CurrentTrack.name)
            print('BPM: ' + str(CurrentTrackTempo))
            SendOSC(IP, Port, "/avatar/parameters/BPM", OSCBPM)
        
        time.sleep(2)
        print('\n' * 3)

if __name__ == "__main__":
    main() 