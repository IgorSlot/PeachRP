from pypresence import Presence
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

RPC = Presence(f"{config['Identifiers']['ClientID']}")
 
RPC.connect()
RPC.update(
    state=f"{config['State']['State']}",
    details=f"{config['State']['Details']}",
    start=f"{config['State']['StartTimestamp']}",
    end=f"{config['State']['EndTimestamp']}",
    large_image=f"{config['Images']['LargeImage']}",
    large_text=f"{config['Images']['LargeImageTooltip']}",
    small_image=f"{config['Images']['SmallImage']}",
    small_text=f"{config['Images']['SmallImageTooltip']}"
)
 
input()