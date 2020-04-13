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

def init_game_power(game):
    game.available_minor_powers = [
        Power("Savage Mawbeasts"              , 0, constants.slow, [constants.fire, constants.animal]),
        Power("Voracious Growth"              , 1, constants.slow, [constants.water, constants.plant]),
        Power("Rouse the Trees and Stones"    , 1, constants.slow, [constants.fire, constants.earth, constants.plant]),
        Power("Encompassing Ward"             , 1, constants.fast, [constants.sun, constants.water, constants.earth]),
        Power("Song of Sanctity"              , 1, constants.slow, [constants.sun, constants.water, constants.plant]),
        Power("Uncanny Melting"               , 1, constants.slow, [constants.sun, constants.moon, constants.water]),
        Power("Shadows of the Burning Forest" , 0, constants.slow, [constants.moon, constants.fire, constants.plant]),
        Power("Steam Vents"                   , 1, constants.fast, [constants.fire, constants.air, constants.water, constants.earth]),
        Power("Veil the Night's Hunt"         , 1, constants.fast, [constants.moon, constants.air, constants.animal]),
        Power("Elemental Boon"                , 1, constants.fast, []),
        Power("Devouring Ants"                , 1, constants.slow, [constants.sun, constants.earth, constants.animal]),
        Power("Dark and Tangled Woods"        , 1, constants.fast, [constants.moon, constants.earth, constants.plant]),
        Power("Sap the Strength of Multitudes", 0, constants.fast, [constants.water, constants.animal]),
        Power("Drift down into Slumber"       , 0, constants.fast, [constants.air, constants.earth, constants.plant]),
        Power("Land of Haunts and Embers"     , 0, constants.fast, [constants.moon, constants.fire, constants.air]),
        Power("Nature's Resilience"           , 1, constants.fast, [constants.earth, constants.plant, constants.animal]),
        Power("Visions of Fiery Doom"         , 1, constants.fast, [constants.moon, constants.fire]),
        Power("Pull Beneath the Hungry Earth" , 1, constants.slow, [constants.moon, constants.water, constants.earth]),
        Power("Call of the Dahan Ways"        , 1, constants.slow, [constants.moon, constants.water, constants.animal]),
        Power("Call to Bloodshed"             , 1, constants.slow, [constants.sun, constants.fire, constants.animal]),
        Power("Call to Isolation"             , 0, constants.fast, [constants.sun, constants.air, constants.animal]),
        Power("Call to Migrate"               , 1, constants.slow, [constants.fire, constants.air, constants.animal]),
        Power("Call to Tend"                  , 1, constants.slow, [constants.water, constants.plant, constants.animal]),
        Power("Quicken the Earth's Struggles" , 1, constants.fast, [constants.moon, constants.fire, constants.earth, constants.animal]),
        Power("Delusions of Danger"           , 1, constants.fast, [constants.sun, constants.moon, constants.air]),
        Power("Drought"                       , 1, constants.slow, [constants.sun, constants.fire, constants.earth]),
        Power("Gift of Constancy"             , 0, constants.fast, [constants.sun, constants.earth]),
        Power("Enticing Splendor"             , 0, constants.fast, [constants.sun, constants.air, constants.plant]),
        Power("Entrancing Apparitions"        , 1, constants.fast, [constants.moon, constants.air, constants.water]),
        Power("Gift of Living Energy"         , 0, constants.fast, [constants.sun, constants.fire, constants.plant]),
        Power("Gift of Power"                 , 0, constants.slow, [constants.moon, constants.water, constants.earth, constants.plant]),
        Power("Gnawing Rootbiters"            , 0, constants.slow, [constants.earth, constants.animal]),
        Power("Lure of the Unknown"           , 0, constants.fast, [constants.moon, constants.fire, constants.air, constants.plant]),
        Power("Purifying Flame"               , 1, constants.slow, [constants.sun, constants.fire, constants.air, constants.plant]),
        Power("Rain of Blood"                 , 0, constants.slow, [constants.air, constants.water, constants.animal]),
        Power("Reaching Grasp"                , 0, constants.fast, [constants.sun, constants.air, constants.water]),
        Power("Inflame the Fires of Life"     , 1, constants.slow, [constants.moon, constants.fire, constants.plant, constants.animal]),
        Power("Fire in the Sky"               , 1, constants.fast, [constants.sun, constants.fire, constants.air]),
        Power("Fleshrot Fever"                , 1, constants.slow, [constants.fire, constants.air, constants.water, constants.animal]),
        Power("Gold's Allure"                 , 0, constants.slow, [constants.fire, constants.earth, constants.animal]),
        Power("Guardian Serpents"             , 1, constants.fast, [constants.sun, constants.moon, constants.earth, constants.animal]),
        Power("Here there be Monsters"        , 0, constants.slow, [constants.moon, constants.air, constants.animal]),
        Power("Infested Aquifers"             , 1, constants.slow, [constants.moon, constants.water, constants.earth, constants.animal]),
        Power("Poisoned Dew"                  , 1, constants.slow, [constants.fire, constants.water, constants.plant]),
        Power("Portents of Disaster"          , 0, constants.fast, [constants.sun, constants.moon, constants.air]),
        Power("Prowling Panthers"             , 1, constants.slow, [constants.moon, constants.fire, constants.animal]),
        Power("Renewing Rain"                 , 1, constants.slow, [constants.water, constants.earth, constants.plant]),
        Power("Rites of the Land's Rejection" , 1, constants.fast, [constants.moon, constants.fire, constants.earth]),
        Power("Pact of the Joined Hunt"       , 1, constants.slow, [constants.sun, constants.plant, constants.animal]),
        Power("Razor-Sharp Undergrowth"       , 1, constants.fast, [constants.moon, constants.plant]),
        Power("Growth through Sacrifice"      , 0, constants.fast, [constants.moon, constants.fire, constants.water, constants.plant]),
        Power("Scour the Land"                , 1, constants.slow, [constants.air, constants.earth]),
        Power("Sky stretches to Shore"        , 1, constants.fast, [constants.sun, constants.air, constants.water, constants.earth]),
        Power("Swarming Wasps"                , 0, constants.fast, [constants.fire, constants.air, constants.animal]),
        Power("Absorb Corruption"             , 1, constants.slow, [constants.sun, constants.earth, constants.plant]),
        Power("Animated Wrackroot"            , 0, constants.slow, [constants.moon, constants.fire, constants.plant]),
        Power("Promises of Protection"        , 0, constants.fast, [constants.sun, constants.earth, constants.animal]),
        Power("Call to Ferocity"              , 0, constants.slow, [constants.sun, constants.fire, constants.earth]),
        Power("Call to Trade"                 , 1, constants.fast, [constants.air, constants.water, constants.earth, constants.plant]),
        Power("Confounding Mists"             , 1, constants.fast, [constants.air, constants.water]),
        Power("Cycles of Time and Tide"       , 1, constants.fast, [constants.sun, constants.moon, constants.water]),
        Power("Disorienting Landscape"        , 1, constants.fast, [constants.moon, constants.air, constants.plant]),
        Power("Elusive Ambushes"              , 1, constants.fast, [constants.sun, constants.fire, constants.water]),
        Power("Tormenting Rotflies"           , 1, constants.slow, [constants.air, constants.plant, constants.animal]),
        Power("Twilight Fog brings Madness"   , 0, constants.slow, [constants.sun, constants.moon, constants.air, constants.water]),
        Power("Teeming Rivers"                , 1, constants.slow, [constants.sun, constants.water, constants.plant, constants.animal]),
        Power("Spur on with Words of Fire"    , 1, constants.fast, [constants.sun, constants.fire, constants.air])
    ]
    game.available_major_powers = [
        Power("Accelerated Rot"                      , 4, constants.slow, [constants.sun, constants.water, constants.plant]),
        Power("Cleansing Floods"                     , 5, constants.slow, [constants.sun, constants.water]),
        Power("Pillar of Living Flame"               , 5, constants.slow, [constants.fire]),
        Power("Poisoned Land"                        , 3, constants.slow, [constants.earth, constants.plant, constants.animal]),
        Power("Terrifying Nightmares"                , 4, constants.fast, [constants.moon, constants.air]),
        Power("The Trees and Stones Speak of War"    , 2, constants.fast, [constants.sun, constants.earth, constants.plant]),
        Power("Entwined Power"                       , 2, constants.fast, [constants.moon, constants.water, constants.plant]),
        Power("Paralyzing Fright"                    , 4, constants.fast, [constants.air, constants.earth]),
        Power("Powerstorm"                           , 3, constants.fast, [constants.sun, constants.fire, constants.air]),
        Power("Talons of Lightning"                  , 6, constants.fast, [constants.fire, constants.air]),
        Power("The Jungle Hungers"                   , 3, constants.slow, [constants.moon, constants.plant]),
        Power("The land Thrashes in Furious Pain"    , 4, constants.slow, [constants.moon, constants.fire, constants.earth]),
        Power("Tsunami"                              , 6, constants.slow, [constants.water, constants.earth]),
        Power("Vigor of the Breaking Dawn"           , 3, constants.fast, [constants.sun, constants.animal]),
        Power("Vengeance of the Dead"                , 3, constants.fast, [constants.moon, constants.fire, constants.animal]),
        Power("Wrap in Wings of Sunlight"            , 3, constants.fast, [constants.sun, constants.air, constants.animal]),
        Power("Blazing Renewal"                      , 5, constants.fast, [constants.fire, constants.earth, constants.plant]),
        Power("Winds of Rust and Atrophy"            , 3, constants.fast, [constants.air, constants.water, constants.animal]),
        Power("Indomitable Claim"                    , 4, constants.fast, [constants.sun, constants.earth]),
        Power("Mists of Oblivion"                    , 4, constants.slow, [constants.moon, constants.air, constants.water]),
        Power("Infinite Vitality"                    , 3, constants.fast, [constants.earth, constants.plant, constants.animal]),
        Power("Dissolve the Bonds of Kinship"        , 4, constants.slow, [constants.fire, constants.water, constants.animal]),
        Power("Strangling Firevine"                  , 4, constants.slow, [constants.fire, constants.plant]),
        Power("Bloodwrack Plague"                    , 4, constants.fast, [constants.water, constants.earth, constants.animal]),
        Power("Cast down into the Briny Deep"        , 9, constants.slow, [constants.sun, constants.moon, constants.water, constants.earth]),
        Power("Death Falls Gently from Open Blossoms", 4, constants.slow, [constants.moon, constants.air, constants.plant]),
        Power("Fire and Flood"                       , 7, constants.slow, [constants.sun, constants.fire, constants.water]),
        Power("Grant Hatred a Ravenous Form"         , 4, constants.slow, [constants.moon, constants.fire]),
        Power("Insatiable Hunger of the Swarm"       , 4, constants.fast, [constants.air, constants.plant, constants.animal]),
        Power("Instruments of their own Ruin"        , 4, constants.fast, [constants.sun, constants.fire, constants.air, constants.animal]),
        Power("Flow like Water, Reach like Air"      , 2, constants.fast, [constants.air, constants.water]),
        Power("Pent-Up Calamity"                     , 3, constants.fast, [constants.moon, constants.fire, constants.earth, constants.plant, constants.animal]),
        Power("Pyroclastic Flow"                     , 3, constants.fast, [constants.fire, constants.air, constants.earth]),
        Power("Savage Transformation"                , 2, constants.slow, [constants.moon, constants.animal]),
        Power("Sea Monsters"                         , 5, constants.slow, [constants.water, constants.animal]),
        Power("Tigers Hunting"                       , 2, constants.fast, [constants.sun, constants.moon, constants.animal]),
        Power("Unrelenting Growth"                   , 4, constants.slow, [constants.sun, constants.fire, constants.water, constants.plant]),
        Power("Volcanic Eruption"                    , 8, constants.slow, [constants.fire, constants.earth]),
        Power("Sweep into the Sea"                   , 4, constants.slow, [constants.sun, constants.air, constants.water]),
        Power("Manifest Incarnation"                 , 6, constants.slow, [constants.sun, constants.moon, constants.earth, constants.animal]),
        Power("Smothering Infestation"               , 3, constants.slow, [constants.water, constants.plant]),
        Power("Twisted Flowers Murmur Ultimatums"    , 5, constants.slow, [constants.sun, constants.moon, constants.air, constants.earth, constants.plant]),
        Power("Unlock the Gates of Deepest Power"    , 4, constants.fast, [constants.sun, constants.moon, constants.fire, constants.air, constants.water, constants.earth, constants.plant, constants.animal])
    ]