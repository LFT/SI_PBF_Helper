# This file contains material owned by Greater Than Games, LLC.
from models.spirit import Spirit
from models.power import Power
import constants

_spirits = dict()
_spirits["Lightning"] = Spirit("Lightning's Swift Strike", [
    Power("Shatter Homesteads"              , 2, constants.slow, [constants.fire, constants.air]),
    Power("Raging Storm"                    , 3, constants.slow, [constants.fire, constants.air, constants.water]),
    Power("Lightning's Boon"                , 1, constants.fast, [constants.fire, constants.air]),
    Power("Harbingers of the Lightning"     , 0, constants.slow, [constants.fire, constants.air])
    ], 1)
_spirits["Shadows"] = Spirit("Shadows Flicker like Flame", [
    Power("Concealing Shadows"              , 0, constants.fast, [constants.moon, constants.air]),
    Power("Mantle of Dread"                 , 1, constants.slow, [constants.moon, constants.fire, constants.air]),
    Power("Favors Called Due"               , 1, constants.slow, [constants.moon, constants.air, constants.animal]),
    Power("Crops Wither and Fade"           , 1, constants.slow, [constants.moon, constants.fire, constants.plant])
    ], 0)
_spirits["Strength"] = Spirit("Vital Strength of the Earth", [
    Power("Guard the Healing Land"          , 3, constants.fast, [constants.water, constants.earth, constants.plant]),
    Power("A Year of Perfect Stillness"     , 3, constants.fast, [constants.sun, constants.earth]),
    Power("Rituals of Destruction"          , 3, constants.slow, [constants.sun, constants.moon, constants.fire, constants.earth, constants.plant]),
    Power("Draw of the Fruitful Earth"      , 1, constants.slow, [constants.earth, constants.plant, constants.animal])
    ], 2)
_spirits["River"] = Spirit("River Surges in Sunlight", [
    Power("Flash Floods"                    , 2, constants.fast, [constants.sun, constants.water]),
    Power("Wash Away"                       , 1, constants.slow, [constants.water, constants.earth]),
    Power("Boon of Vigor"                   , 0, constants.fast, [constants.sun, constants.water, constants.plant]),
    Power("River's Bounty"                  , 0, constants.slow, [constants.sun, constants.water, constants.animal])
    ], 1)
_spirits["Thunderspeaker"] = Spirit("Thunderspeaker", [
    Power("Manifestation of Power and Glory", 3, constants.slow, [constants.sun, constants.fire, constants.air]),
    Power("Words of Warning"                , 1, constants.fast, [constants.sun, constants.air, constants.animal]),
    Power("Sudden Ambush"                   , 2, constants.fast, [constants.fire, constants.air, constants.animal]),
    Power("Voice of Thunder"                , 0, constants.slow, [constants.sun, constants.air])
    ], 1)
_spirits["Spread"] = Spirit("A Spread of Rampant Green", [
    Power("Overgrow in a Night"             , 2, constants.fast, [constants.moon, constants.plant]),
    Power("Gift of Proliferation"           , 1, constants.fast, [constants.moon, constants.plant]),
    Power("Fields Choked with Growth"       , 0, constants.slow, [constants.sun, constants.water, constants.plant]),
    Power("Stem the Flow of Fresh Water"    , 0, constants.slow, [constants.water, constants.plant])
    ], 0)
_spirits["Bringer"] = Spirit("Bringer of Dreams and Nightmare", [
    Power("Predatory Nightmares"            , 2, constants.slow, [constants.moon, constants.fire, constants.earth, constants.animal]),
    Power("Dread Apparitions"               , 2, constants.fast, [constants.moon, constants.air]),
    Power("Call on Midnight's Dreams"       , 0, constants.fast, [constants.moon, constants.animal]),
    Power("Dreams of the Dahan"             , 0, constants.fast, [constants.moon, constants.air])
    ], 2)
_spirits["Ocean"] = Spirit("Ocean's Hungry Grasp", [
    Power("Call of the Deeps"               , 0, constants.fast, [constants.moon, constants.air, constants.water]),
    Power("Grasping Tide"                   , 1, constants.fast, [constants.moon, constants.water]),
    Power("Swallow the Land-Dwellers"       , 0, constants.slow, [constants.water, constants.earth]),
    Power("Tidal Boon"                      , 1, constants.slow, [constants.moon, constants.water, constants.earth])
    ], 0)
_spirits["Fangs"] = Spirit("Sharp Fangs behind the Leaves", [
    Power("Prey on the Builders"        , 1, constants.fast, [constants.moon, constants.fire, constants.animal]),
    Power("Teeth Gleam from Darkness"   , 1, constants.slow, [constants.moon, constants.plant, constants.animal]),
    Power("Too near the Jungle"         , 0, constants.slow, [constants.plant, constants.animal]),
    Power("Terrifying Chase"            , 1, constants.slow, [constants.sun, constants.animal])
    ], 1)
_spirits["Keeper"] = Spirit("Keeper of the forbidden wilds", [
    Power("Towering Wrath"              , 3, constants.slow, [constants.sun, constants.fire, constants.plant]),
    Power("Regrow from Roots"           , 1, constants.slow, [constants.water, constants.earth, constants.plant]),
    Power("Boon of Growing Power"       , 1, constants.slow, [constants.sun, constants.moon, constants.plant]),
    Power("Sacrosanct Wilderness"       , 2, constants.fast, [constants.sun, constants.earth, constants.plant])
    ], 2)
_spirits["Serpent"] = Spirit("Serpent Slumbering beneath the Island", [
    Power("Gift of the Primordial Deeps", 1, constants.fast, [constants.moon, constants.earth]),
    Power("Gift of Flowing Power"       , 1, constants.fast, [constants.fire, constants.water]),
    Power("Absorb Essence"              , 2, constants.fast, [constants.moon, constants.fire, constants.water, constants.earth]),
    Power("Elemental Aegis"             , 1, constants.fast, [constants.fire, constants.water, constants.earth])
    ], 1)
_spirits["Heart"] = Spirit("Heart of the Wildfire", [
    Power("Flash-Fires"                 , 2, constants.slow, [constants.fire, constants.air]),
    Power("Asphyxiating Smoke"          , 2, constants.slow, [constants.fire, constants.air, constants.plant]),
    Power("Flame's Fury"                , 0, constants.fast, [constants.sun, constants.fire, constants.plant]),
    Power("Threatening Flames"          , 0, constants.fast, [constants.fire, constants.plant]),
    ], 2)

def get_spirit(spirit):
    return _spirits[spirit]