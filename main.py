from pypresence import Presence
import configparser

config = configparser.ConfigParser()
config.read('config.ini') 

RPC = Presence(f"{config['Identifiers']['ClientID']}")
 
RPC.connect()
RPC.update(
    state=None if f"{config['State']['State']}" == "" else f"{config['State']['State']}",
    details=None if f"{config['State']['Details']}" == "" else f"{config['State']['Details']}",
    start=None if f"{config['State']['StartTimestamp']}" == "" else f"{config['State']['StartTimestamp']}",
    end=None if f"{config['State']['EndTimestamp']}" == "" else f"{config['State']['EndTimestamp']}",
    large_image=None if f"{config['Images']['LargeImage']}" == "" else f"{config['Images']['LargeImage']}",
    large_text=None if f"{config['Images']['LargeImageTooltip']}" == "" else f"{config['Images']['LargeImageTooltip']}",
    small_image=None if f"{config['Images']['SmallImage']}" == "" else f"{config['Images']['SmallImage']}",
    small_text=None if f"{config['Images']['SmallImageTooltip']}" == "" else f"{config['Images']['SmallImageTooltip']}"
)
 
input()
