# This file contains material owned by Greater Than Games, LLC.
from models.spirit import Spirit
from models.power import Power
import constants
import random

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

def init_game_power(game):
    game.available_minor_powers = [
        Power("Savage Mawbeasts"              , 0, constants.slow, [constants.fire, constants.animal], constants.minor),
        Power("Voracious Growth"              , 1, constants.slow, [constants.water, constants.plant], constants.minor),
        Power("Rouse the Trees and Stones"    , 1, constants.slow, [constants.fire, constants.earth, constants.plant], constants.minor),
        Power("Encompassing Ward"             , 1, constants.fast, [constants.sun, constants.water, constants.earth] , constants.minor),
        Power("Song of Sanctity"              , 1, constants.slow, [constants.sun, constants.water, constants.plant] , constants.minor),
        Power("Uncanny Melting"               , 1, constants.slow, [constants.sun, constants.moon, constants.water]  , constants.minor),
        Power("Shadows of the Burning Forest" , 0, constants.slow, [constants.moon, constants.fire, constants.plant] , constants.minor),
        Power("Steam Vents"                   , 1, constants.fast, [constants.fire, constants.air, constants.water, constants.earth], constants.minor),
        Power("Veil the Night's Hunt"         , 1, constants.fast, [constants.moon, constants.air, constants.animal], constants.minor),
        Power("Elemental Boon"                , 1, constants.fast, [], constants.minor),
        Power("Devouring Ants"                , 1, constants.slow, [constants.sun, constants.earth, constants.animal], constants.minor),
        Power("Dark and Tangled Woods"        , 1, constants.fast, [constants.moon, constants.earth, constants.plant], constants.minor),
        Power("Sap the Strength of Multitudes", 0, constants.fast, [constants.water, constants.animal], constants.minor),
        Power("Drift down into Slumber"       , 0, constants.fast, [constants.air, constants.earth, constants.plant], constants.minor),
        Power("Land of Haunts and Embers"     , 0, constants.fast, [constants.moon, constants.fire, constants.air], constants.minor),
        Power("Nature's Resilience"           , 1, constants.fast, [constants.earth, constants.plant, constants.animal], constants.minor),
        Power("Visions of Fiery Doom"         , 1, constants.fast, [constants.moon, constants.fire], constants.minor),
        Power("Pull Beneath the Hungry Earth" , 1, constants.slow, [constants.moon, constants.water, constants.earth] , constants.minor),
        Power("Call of the Dahan Ways"        , 1, constants.slow, [constants.moon, constants.water, constants.animal], constants.minor),
        Power("Call to Bloodshed"             , 1, constants.slow, [constants.sun, constants.fire, constants.animal], constants.minor),
        Power("Call to Isolation"             , 0, constants.fast, [constants.sun, constants.air, constants.animal], constants.minor),
        Power("Call to Migrate"               , 1, constants.slow, [constants.fire, constants.air, constants.animal], constants.minor),
        Power("Call to Tend"                  , 1, constants.slow, [constants.water, constants.plant, constants.animal], constants.minor),
        Power("Quicken the Earth's Struggles" , 1, constants.fast, [constants.moon, constants.fire, constants.earth, constants.animal], constants.minor),
        Power("Delusions of Danger"           , 1, constants.fast, [constants.sun, constants.moon, constants.air], constants.minor),
        Power("Drought"                       , 1, constants.slow, [constants.sun, constants.fire, constants.earth], constants.minor),
        Power("Gift of Constancy"             , 0, constants.fast, [constants.sun, constants.earth], constants.minor),
        Power("Enticing Splendor"             , 0, constants.fast, [constants.sun, constants.air, constants.plant], constants.minor),
        Power("Entrancing Apparitions"        , 1, constants.fast, [constants.moon, constants.air, constants.water], constants.minor),
        Power("Gift of Living Energy"         , 0, constants.fast, [constants.sun, constants.fire, constants.plant], constants.minor),
        Power("Gift of Power"                 , 0, constants.slow, [constants.moon, constants.water, constants.earth, constants.plant], constants.minor),
        Power("Gnawing Rootbiters"            , 0, constants.slow, [constants.earth, constants.animal], constants.minor),
        Power("Lure of the Unknown"           , 0, constants.fast, [constants.moon, constants.fire, constants.air, constants.plant], constants.minor),
        Power("Purifying Flame"               , 1, constants.slow, [constants.sun, constants.fire, constants.air, constants.plant], constants.minor),
        Power("Rain of Blood"                 , 0, constants.slow, [constants.air, constants.water, constants.animal], constants.minor),
        Power("Reaching Grasp"                , 0, constants.fast, [constants.sun, constants.air, constants.water], constants.minor),
        Power("Inflame the Fires of Life"     , 1, constants.slow, [constants.moon, constants.fire, constants.plant, constants.animal], constants.minor),
        Power("Fire in the Sky"               , 1, constants.fast, [constants.sun, constants.fire, constants.air], constants.minor),
        Power("Fleshrot Fever"                , 1, constants.slow, [constants.fire, constants.air, constants.water, constants.animal], constants.minor),
        Power("Gold's Allure"                 , 0, constants.slow, [constants.fire, constants.earth, constants.animal], constants.minor),
        Power("Guardian Serpents"             , 1, constants.fast, [constants.sun, constants.moon, constants.earth, constants.animal], constants.minor),
        Power("Here there be Monsters"        , 0, constants.slow, [constants.moon, constants.air, constants.animal], constants.minor),
        Power("Infested Aquifers"             , 1, constants.slow, [constants.moon, constants.water, constants.earth, constants.animal], constants.minor),
        Power("Poisoned Dew"                  , 1, constants.slow, [constants.fire, constants.water, constants.plant], constants.minor),
        Power("Portents of Disaster"          , 0, constants.fast, [constants.sun, constants.moon, constants.air], constants.minor),
        Power("Prowling Panthers"             , 1, constants.slow, [constants.moon, constants.fire, constants.animal], constants.minor),
        Power("Renewing Rain"                 , 1, constants.slow, [constants.water, constants.earth, constants.plant], constants.minor),
        Power("Rites of the Land's Rejection" , 1, constants.fast, [constants.moon, constants.fire, constants.earth], constants.minor),
        Power("Pact of the Joined Hunt"       , 1, constants.slow, [constants.sun, constants.plant, constants.animal], constants.minor),
        Power("Razor-Sharp Undergrowth"       , 1, constants.fast, [constants.moon, constants.plant], constants.minor),
        Power("Growth through Sacrifice"      , 0, constants.fast, [constants.moon, constants.fire, constants.water, constants.plant], constants.minor),
        Power("Scour the Land"                , 1, constants.slow, [constants.air, constants.earth], constants.minor),
        Power("Sky stretches to Shore"        , 1, constants.fast, [constants.sun, constants.air, constants.water, constants.earth], constants.minor),
        Power("Swarming Wasps"                , 0, constants.fast, [constants.fire, constants.air, constants.animal], constants.minor),
        Power("Absorb Corruption"             , 1, constants.slow, [constants.sun, constants.earth, constants.plant], constants.minor),
        Power("Animated Wrackroot"            , 0, constants.slow, [constants.moon, constants.fire, constants.plant], constants.minor),
        Power("Promises of Protection"        , 0, constants.fast, [constants.sun, constants.earth, constants.animal], constants.minor),
        Power("Call to Ferocity"              , 0, constants.slow, [constants.sun, constants.fire, constants.earth], constants.minor),
        Power("Call to Trade"                 , 1, constants.fast, [constants.air, constants.water, constants.earth, constants.plant], constants.minor),
        Power("Confounding Mists"             , 1, constants.fast, [constants.air, constants.water], constants.minor),
        Power("Cycles of Time and Tide"       , 1, constants.fast, [constants.sun, constants.moon, constants.water], constants.minor),
        Power("Disorienting Landscape"        , 1, constants.fast, [constants.moon, constants.air, constants.plant], constants.minor),
        Power("Elusive Ambushes"              , 1, constants.fast, [constants.sun, constants.fire, constants.water], constants.minor),
        Power("Tormenting Rotflies"           , 1, constants.slow, [constants.air, constants.plant, constants.animal], constants.minor),
        Power("Twilight Fog brings Madness"   , 0, constants.slow, [constants.sun, constants.moon, constants.air, constants.water], constants.minor),
        Power("Teeming Rivers"                , 1, constants.slow, [constants.sun, constants.water, constants.plant, constants.animal], constants.minor),
        Power("Spur on with Words of Fire"    , 1, constants.fast, [constants.sun, constants.fire, constants.air], constants.minor)
    ]
    random.shuffle(game.available_minor_powers)
    game.available_major_powers = [
        Power("Accelerated Rot"                      , 4, constants.slow, [constants.sun, constants.water, constants.plant], constants.major),
        Power("Cleansing Floods"                     , 5, constants.slow, [constants.sun, constants.water], constants.major),
        Power("Pillar of Living Flame"               , 5, constants.slow, [constants.fire], constants.major),
        Power("Poisoned Land"                        , 3, constants.slow, [constants.earth, constants.plant, constants.animal], constants.major),
        Power("Terrifying Nightmares"                , 4, constants.fast, [constants.moon, constants.air], constants.major),
        Power("The Trees and Stones Speak of War"    , 2, constants.fast, [constants.sun, constants.earth, constants.plant], constants.major),
        Power("Entwined Power"                       , 2, constants.fast, [constants.moon, constants.water, constants.plant], constants.major),
        Power("Paralyzing Fright"                    , 4, constants.fast, [constants.air, constants.earth], constants.major),
        Power("Powerstorm"                           , 3, constants.fast, [constants.sun, constants.fire, constants.air], constants.major),
        Power("Talons of Lightning"                  , 6, constants.fast, [constants.fire, constants.air], constants.major),
        Power("The Jungle Hungers"                   , 3, constants.slow, [constants.moon, constants.plant], constants.major),
        Power("The land Thrashes in Furious Pain"    , 4, constants.slow, [constants.moon, constants.fire, constants.earth], constants.major),
        Power("Tsunami"                              , 6, constants.slow, [constants.water, constants.earth], constants.major),
        Power("Vigor of the Breaking Dawn"           , 3, constants.fast, [constants.sun, constants.animal], constants.major),
        Power("Vengeance of the Dead"                , 3, constants.fast, [constants.moon, constants.fire, constants.animal], constants.major),
        Power("Wrap in Wings of Sunlight"            , 3, constants.fast, [constants.sun, constants.air, constants.animal], constants.major),
        Power("Blazing Renewal"                      , 5, constants.fast, [constants.fire, constants.earth, constants.plant], constants.major),
        Power("Winds of Rust and Atrophy"            , 3, constants.fast, [constants.air, constants.water, constants.animal], constants.major),
        Power("Indomitable Claim"                    , 4, constants.fast, [constants.sun, constants.earth], constants.major),
        Power("Mists of Oblivion"                    , 4, constants.slow, [constants.moon, constants.air, constants.water], constants.major),
        Power("Infinite Vitality"                    , 3, constants.fast, [constants.earth, constants.plant, constants.animal], constants.major),
        Power("Dissolve the Bonds of Kinship"        , 4, constants.slow, [constants.fire, constants.water, constants.animal], constants.major),
        Power("Strangling Firevine"                  , 4, constants.slow, [constants.fire, constants.plant], constants.major),
        Power("Bloodwrack Plague"                    , 4, constants.fast, [constants.water, constants.earth, constants.animal], constants.major),
        Power("Cast down into the Briny Deep"        , 9, constants.slow, [constants.sun, constants.moon, constants.water, constants.earth], constants.major),
        Power("Death Falls Gently from Open Blossoms", 4, constants.slow, [constants.moon, constants.air, constants.plant], constants.major),
        Power("Fire and Flood"                       , 7, constants.slow, [constants.sun, constants.fire, constants.water], constants.major),
        Power("Grant Hatred a Ravenous Form"         , 4, constants.slow, [constants.moon, constants.fire], constants.major),
        Power("Insatiable Hunger of the Swarm"       , 4, constants.fast, [constants.air, constants.plant, constants.animal], constants.major),
        Power("Instruments of their own Ruin"        , 4, constants.fast, [constants.sun, constants.fire, constants.air, constants.animal], constants.major),
        Power("Flow like Water, Reach like Air"      , 2, constants.fast, [constants.air, constants.water], constants.major),
        Power("Pent-Up Calamity"                     , 3, constants.fast, [constants.moon, constants.fire, constants.earth, constants.plant, constants.animal], constants.major),
        Power("Pyroclastic Flow"                     , 3, constants.fast, [constants.fire, constants.air, constants.earth], constants.major),
        Power("Savage Transformation"                , 2, constants.slow, [constants.moon, constants.animal], constants.major),
        Power("Sea Monsters"                         , 5, constants.slow, [constants.water, constants.animal], constants.major),
        Power("Tigers Hunting"                       , 2, constants.fast, [constants.sun, constants.moon, constants.animal], constants.major),
        Power("Unrelenting Growth"                   , 4, constants.slow, [constants.sun, constants.fire, constants.water, constants.plant], constants.major),
        Power("Volcanic Eruption"                    , 8, constants.slow, [constants.fire, constants.earth], constants.major),
        Power("Sweep into the Sea"                   , 4, constants.slow, [constants.sun, constants.air, constants.water], constants.major),
        Power("Manifest Incarnation"                 , 6, constants.slow, [constants.sun, constants.moon, constants.earth, constants.animal], constants.major),
        Power("Smothering Infestation"               , 3, constants.slow, [constants.water, constants.plant], constants.major),
        Power("Twisted Flowers Murmur Ultimatums"    , 5, constants.slow, [constants.sun, constants.moon, constants.air, constants.earth, constants.plant], constants.major),
        Power("Unlock the Gates of Deepest Power"    , 4, constants.fast, [constants.sun, constants.moon, constants.fire, constants.air, constants.water, constants.earth, constants.plant, constants.animal], constants.major)
    ]
    random.shuffle(game.available_major_powers)