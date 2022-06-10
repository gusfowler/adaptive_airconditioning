# adaptive_airconditioning

This is a python script for homeassistant that will keep your thermostat set to exactly X degrees under the outside temperature (X being the value you assign)

The idea is that most home air conditioning units can only sustain an inside temperature 20/30 degrees, so this script does it's best to do that. I put a floor and ceiling in, idea that the floor is what you want the temperature to be in good conditions, and the ceiling is the maximum temperature that you allow the ceiling to go to.

I wrote this while my air conditioner was locking up in an Arizona heatwave :)

In your homeassistant configuration.yaml you need to have a line that is 'python_script:' - there is no switch in the UI to just enable this.

Then in your configuration folder (usually /config), create a directory 'python_scripts' and copy 'adaptive_ac.py' and 'services.yaml' (or append the contents to your preexisting services file) into 'python_scripts'

Reload HA and you should be good to go. I have provided a sample automation to get you started.
* Note: each time the script runs, it will apply the temperature determined to be best, so if you have it run every 15 minutes, if you turn off your air conditioner without disabling your automation setup, it will turn it back on 

Sources:
https://www.home-assistant.io

## I AM NOT LIABLE IF YOUR AIRCONDITION BLOWS UP - use at own risk
While I consider myself pretty knowledgeable with electronics, I am not a licensed electrician, certified air condition serviceman, etc. I also, as of the time of writing this, have only debugged this live for a few days of running.