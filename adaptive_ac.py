# Pull in information passed from Home Assistant
#Entities
thermostat_entity = data.get('thermostat_entity')
outside_temperature_entity = data.get('outside_temperature_entity')
indoor_temperature_entity = data.get('indoor_temperature_entity')

#Values
temp_diff_value = data.get('temp_diff_value')
maximum_set_temperature = data.get('maximum_set_temperature')
target_temperature = data.get('target_temperature')

logger.info("Adaptive A/C executing")

## If logged to info then it is for debugging / devel, and left in for if anyone else needs help changing it later

logger.info(thermostat_entity)
logger.info(outside_temperature_entity)
logger.info(indoor_temperature_entity)

logger.info("Temperature Difference: " + str(temp_diff_value))
logger.info("Max Temp: " + str(maximum_set_temperature))
logger.info("Target Temp: " + str(target_temperature))

outsideTemp = int(float(hass.states.get(outside_temperature_entity).state)) # int(float(x)) to drop decimal
insideTemp = int(float(hass.states.get(indoor_temperature_entity).state))

logger.info("Inside Temp: " + str(insideTemp))
logger.info("Outside Temp: " + str(outsideTemp))

tempDiff = int(temp_diff_value)
maxTemp = int(maximum_set_temperature)
targetTemp = int(target_temperature)

def setTemp(thermostatEntity, newTemp):
    hass.services.call('climate', 'set_temperature', 
        {
            'entity_id': thermostatEntity,
            'temperature': newTemp,
            'hvac_mode': 'cool'
        }, False)
    logger.info("setTemp set temperature to " + str(newTemp))


# outside temperature outside A/C capacity
if (targetTemp + tempDiff) < outsideTemp:
    newTargetTemp = outsideTemp - tempDiff
    if newTargetTemp > maxTemp: newTargetTemp = maxTemp
    elif newTargetTemp < targetTemp: newTargetTemp = targetTemp # should be unreachable but I had an error on my part where it was so I left it
    logger.info("newTargetTemp: " + str(newTargetTemp))
    # set Temperature
    setTemp(thermostat_entity, newTargetTemp)
else:
    currentTargetTemp = int(hass.states.get(thermostat_entity).attributes['temperature'])
    logger.info("currentTargetTemp: " + str(currentTargetTemp))
    if targetTemp < currentTargetTemp:
        logger.info("targetTemp is less than currentTargetTemp")
        # set Temperature
        setTemp(thermostat_entity, targetTemp)
    else:
        logger.info("targetTemp is greater than currentTargetTemp")
        # set Temperature
        setTemp(thermostat_entity, targetTemp)