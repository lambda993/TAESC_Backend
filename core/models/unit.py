from django.db import models
from django.utils.translation import gettext_lazy as _
from coreutils.models import CoreModel
from core.models import (
    Corpse, Footprint, MovementClass,
    SoundCategory, TEDClass, UnitCategory,
    UnitOrder, UnitSide, Weapon
)


class Unit(CoreModel):
    unit_name = models.CharField(verbose_name=_('Unit name'),
                                 max_length=20, help_text=_('Unit ingame ID code.'))
    unit_number = models.IntegerField(verbose_name=_(
        'Unit number'), help_text=_('Ingame unit ID.'))
    commander = models.BooleanField(verbose_name=_('Commander'),
                                    default=False, help_text=_('If game ends ruleset is selected, the death of this unit will end the game.'))
    show_player_name = models.BooleanField(verbose_name=_('Show player name'),
                                           default=False, help_text=_("Player's name will replace this unit's name."))
    name = models.CharField(verbose_name=_('Name'), max_length=50, help_text=_(
        'Name of the unit displayed ingame.'))
    description = models.TextField(verbose_name=_(
        'Description'), help_text=_('Unit ingame description.'))
    side = models.ForeignKey(
        UnitSide, on_delete=models.PROTECT, related_name="unit_side", verbose_name=_('Side'))
    designation = models.CharField(verbose_name=_('Designation'),
                                   max_length=20, blank=True, help_text=_('Unit 3D model name.'))
    footprint = models.ForeignKey(Footprint, on_delete=models.PROTECT, related_name='units_footprint', verbose_name=_(
        'Footprint'), help_text=_('Unit footprint on X and Z coordinates.'))
    hide_damage = models.BooleanField(verbose_name=_('Hide damage'),
                                      default=False, help_text=_("Hide unit's health bar."))
    immune_to_paralyze = models.BooleanField(verbose_name=_('Immune to paralyze'),
                                             default=False, help_text=_('This unit is immune to stun weapons'))
    stealth = models.BooleanField(verbose_name=_('Stealth'),
                                  default=False, help_text=_('This unit is invisible to enemy radar.'))
    category = models.ManyToManyField(
        UnitCategory, related_name="unit_category", verbose_name=_('Category'), help_text=_('List of categories that this unit is represented by.'))
    bad_target_category = models.ForeignKey(
        UnitCategory, on_delete=models.PROTECT, related_name="unit_bad_target_category", null=True, blank=True, verbose_name=_('Bad target category'), help_text=_('Category this unit will have a hard time engaging.'))
    no_chase_category = models.ForeignKey(
        UnitCategory, on_delete=models.PROTECT, related_name="unit_no_chase_category", null=True, blank=True, verbose_name=_('No chase category'), help_text=_('Category this will not chase after when out of range.'))
    editor_class = models.ForeignKey(
        TEDClass, on_delete=models.PROTECT, related_name="unit_tedclass", verbose_name=_('Editor class'), help_text=_('Category in which this unit is placed in the Total Annihilation Map Editor.'))
    sound_category = models.ForeignKey(SoundCategory, on_delete=models.PROTECT, related_name="units_sound_category", verbose_name=_(
        'Sound category'), help_text=_('Category of sounds this unit will play.'))
    default_orders = models.ForeignKey(
        UnitOrder, on_delete=models.PROTECT, related_name="unit_orders", verbose_name=_('Default orders'), help_text=_('How this unit behaves once built.'))
    explode_as = models.ForeignKey(Weapon, on_delete=models.PROTECT, related_name="units_explode_as", verbose_name=_(
        'Explode as'), help_text=_('Weapon that fires when unit is killed.'))
    self_destruct_as = models.ForeignKey(Weapon, on_delete=models.PROTECT, related_name="units_self_destruct_as", verbose_name=_(
        'Self destruct as'), help_text=_('Weapon that is fired when unit dies by self destruction.'))
    corpse = models.ForeignKey(Corpse, on_delete=models.PROTECT, related_name="units_corpse", verbose_name=_(
        'Corpse'), help_text=_('Corpse left on the map after unit death.'))
    self_destruct_countdown = models.SmallIntegerField(verbose_name=_('Self destruct countdown'), help_text=_('Seconds until this unit self destructs.'),
                                                       null=True, blank=True, default=5)
    shoot_me = models.BooleanField(verbose_name=_('Shoot me'),
                                   default=False, help_text=_('This unit is engaged automatically when in range.'))
    antiweapons = models.BooleanField(verbose_name=_('Anti weapons'),
                                      default=False, help_text=_('This unit has anti-nuke weapons (used to make white rings on the map).'))
    amphibious = models.BooleanField(verbose_name=_('Amphibious'),
                                     default=False, help_text=_('This unit can go underwater.'))
    floater = models.BooleanField(verbose_name=_('Floater'),
                                  default=False, help_text=_('This unit can be engaged by torpedo weapons.'))
    digger = models.BooleanField(verbose_name=_('Digger'),
                                 default=False, help_text=_('This unit is partially undergound.'))
    can_fly = models.BooleanField(verbose_name=_('Can fly'),
                                  default=False, help_text=_('This unit is immune to ground damage explosions.'))
    can_hover = models.BooleanField(verbose_name=_('Can hover'),
                                    default=False, help_text=_('This unit hovers over water, cannot be engaged by torpedo weapons.'))
    is_airbase = models.BooleanField(verbose_name=_('Is airbase'),
                                     default=False, help_text=_('Aircraft can land on this unit for repairs.'))
    is_feature = models.BooleanField(verbose_name=_('Is feature'),
                                     default=False, help_text=_('This unit will become a map feature when built and will not count towards unit limit.'))
    is_targeting_upgrade = models.BooleanField(verbose_name=_('Is targeting upgrade'),
                                               default=False, help_text=_('This unit will upgrade commanders and allow autonomous fire on units that are detected by radar/sonar.'))

    def __str__(self):
        return f'{self.unit_name} ({self.side.name} {self.name})'

    class Meta:
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')
        ordering = ('-game_version', 'unit_name', 'unit_number')
        unique_together = (('game_version', 'unit_name'),
                           ('game_version', 'unit_name', 'unit_number'))


class UnitSightOption(CoreModel):
    unit = models.OneToOneField(Unit, on_delete=models.PROTECT,
                                related_name='unit_sight_option', verbose_name=_('Unit'))
    sight_distance = models.IntegerField(verbose_name=_(
        'Sight distance'), help_text=_('How far is this unit able to see.'))
    radar_distance = models.IntegerField(verbose_name=_('Radar distance'), help_text=_(
        'How far this unit spots non submerged enemies on the map.'), null=True, blank=True, default=0)
    radar_jammer = models.IntegerField(verbose_name=_('Radar jammer'), help_text=_(
        'How far this unit jams enemy radar.'), null=True, blank=True, default=0)
    sonar_distance = models.IntegerField(verbose_name=_('Sonar distance'), help_text=_(
        'How far this unit spots sumberged enemies on the map.'), null=True, blank=True, default=0)
    sonar_jammer = models.IntegerField(verbose_name=_('Sonar jammer'), help_text=_(
        'How far this unit jams enemy sonar.'), null=True, blank=True, default=0)

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = _('Unit sight option')
        verbose_name_plural = _('Unit sight options')
        ordering = ('-game_version', 'unit')
        unique_together = ('game_version', 'unit')


class UnitWeaponGroup(CoreModel):
    unit = models.OneToOneField(Unit, on_delete=models.PROTECT,
                                related_name='unit_weapon_group', verbose_name=_('Unit'))
    weapon1 = models.ForeignKey(Weapon, on_delete=models.PROTECT,
                                related_name="units_weapon1", verbose_name=_('Weapon 1'))
    weapon1_bad_target = models.ForeignKey(
        UnitCategory, on_delete=models.PROTECT, related_name="unit_w1_bad_target", null=True, blank=True, verbose_name=_('Weapon 1 bad targeting category'))
    weapon2 = models.ForeignKey(Weapon, on_delete=models.PROTECT,
                                related_name="units_weapon2", verbose_name=_('Weapon 2'))
    weapon2_bad_target = models.ForeignKey(
        UnitCategory, on_delete=models.PROTECT, related_name="unit_w2_bad_target", null=True, blank=True, verbose_name=_('Weapon 2 bad targeting category'))
    weapon3 = models.ForeignKey(Weapon, on_delete=models.PROTECT,
                                related_name="units_weapon3", verbose_name=_('Weapon 3'))
    weapon3_bad_target = models.ForeignKey(
        UnitCategory, on_delete=models.PROTECT, related_name="unit_w3_bad_target", null=True, blank=True, verbose_name=_('Weapon 3 bad targeting category'))

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = _('Unit weapon group')
        verbose_name_plural = _('Unit weapon groups')
        ordering = ('-game_version', 'unit')
        unique_together = ('game_version', 'unit')


class UnitEconomy(CoreModel):
    unit = models.OneToOneField(Unit, on_delete=models.PROTECT,
                                related_name='unit_economy', verbose_name=_('Unit'))
    energy_use = models.DecimalField(verbose_name=_('Energy use'), help_text=_('Amount of energy used by this unit to function.'),
                                     max_digits=20, decimal_places=10, default=0)
    metal_use = models.DecimalField(verbose_name=_('Metal use'), help_text=_('Amount of metal used by this unit to functio.'),
                                    max_digits=20, decimal_places=10, default=0)
    energy_make = models.DecimalField(verbose_name=_('Energy make'), help_text=_('Amount of energy produced by this unit.'),
                                      max_digits=20, decimal_places=10, default=0)
    metal_make = models.DecimalField(verbose_name=_('Metal make'), help_text=_('Amount of metal produced by this unit.'),
                                     max_digits=20, decimal_places=10, default=0)
    energy_store = models.IntegerField(default=0, verbose_name=_(
        'Energy store'), help_text=_('Amount of energy storage generated by this unit.'))
    metal_store = models.IntegerField(default=0, verbose_name=_(
        'Metal store'), help_text=_('Amount of metal storage generated by this unit.'))

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = _('Unit economy')
        verbose_name_plural = _('Unit economies')
        ordering = ('-game_version', 'unit')
        unique_together = ('game_version', 'unit')


class UnitBasicStat(CoreModel):
    unit = models.OneToOneField(Unit, on_delete=models.PROTECT,
                                related_name='unit_basic_stats', verbose_name=_('Unit'))
    build_energy_cost = models.IntegerField(verbose_name=_(
        'Build energy cost'), help_text=_('Total energy needed to build this unit.'))
    build_metal_cost = models.IntegerField(verbose_name=_(
        'Build metal cost'), help_text=_('Total metal needed to build this unit.'))
    build_time_cost = models.IntegerField(verbose_name=_('Build cost time'), help_text=_(
        'Total time in ingame ticks needed to build this unit.'))
    max_damage = models.IntegerField(verbose_name=_(
        'Max damage'), help_text=_('Unit health points'))
    damage_modifier = models.DecimalField(verbose_name=_('Damage modifier'),
                                          max_digits=20, decimal_places=10, default=1, help_text=_('Damage reduction that is applied to the unit when hit.'))
    heal_time = models.IntegerField(verbose_name=_('Heal time'), help_text=_(
        'Amount of health regained per game tick.'), null=True, blank=True, default=0)

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = _('Unit basic stat')
        verbose_name_plural = _('Unit basic stats')
        ordering = ('-game_version', 'unit')
        unique_together = ('game_version', 'unit')


class UnitBuilder(CoreModel):
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT,
                             related_name='units_builder', verbose_name=_('Unit'))
    worker_time = models.IntegerField(verbose_name=_(
        'Worker time'), help_text=_('Building speed of the unit per game tick.'))
    build_distance = models.IntegerField(verbose_name=_(
        'Build distance'), help_text=_('How far can this unit build from.'))
    can_resurrect = models.BooleanField(
        verbose_name=_('Can resurrect'), default=False)
    can_capture = models.BooleanField(
        verbose_name=_('Can capture'), default=False)

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = _('Unit builder')
        verbose_name_plural = _('Unit builders')
        ordering = ('-game_version', 'unit')
        unique_together = ('game_version', 'unit')


class UnitTransporter(CoreModel):
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT,
                             related_name='units_transporter', verbose_name=_('Unit'))
    transport_size = models.SmallIntegerField(verbose_name=_(
        'Transport size'), help_text=_('Amount of units this transporter can load at once.'))
    transport_capacity = models.SmallIntegerField(verbose_name=_(
        'Transport capacity'), help_text=_('Transport footprint for each unit.'))
    transport_max_units = models.SmallIntegerField(verbose_name=_(
        'Transport max units'), help_text=_('Maximum total unit transported footprint.'))

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = _('Unit transporter')
        verbose_name_plural = _('Unit transporters')
        ordering = ('-game_version', 'unit')
        unique_together = ('game_version', 'unit')


class UnitBuilding(CoreModel):
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT,
                             related_name='units_building', verbose_name=_('Unit'))
    yard_map = models.TextField(verbose_name=_('Yard map'),
                                blank=True, help_text=_('Map of how the game engine handles collisions'))

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = _('Unit building')
        verbose_name_plural = _('Unit buildings')
        ordering = ('-game_version', 'unit')
        unique_together = ('game_version', 'unit')


class UnitKamikaze(CoreModel):
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT,
                             related_name='units_kamikaze', verbose_name=_('Unit'))
    kamikaze_distance = models.SmallIntegerField(verbose_name=_('Kamikaze distance'), help_text=_(
        'Minimum distance at wich a suicider unit will self destruct.'))

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = _('Unit kamikaze')
        verbose_name_plural = _('Unit kamikazes')
        ordering = ('-game_version', 'unit')
        unique_together = ('game_version', 'unit')


class UnitMovement(CoreModel):
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT,
                             related_name='units_movement', verbose_name=_('Unit'))
    movement_class = models.ForeignKey(
        MovementClass, on_delete=models.PROTECT, related_name='units_movement_class', verbose_name=_('Movement class'), help_text=_('Ingame class on how this unit maneuvers on the map.'))
    max_velocity = models.DecimalField(verbose_name=_('Max velocity'), help_text=_('Maximum velocity the unit can attain.'),
                                       max_digits=20, decimal_places=10, default=0)
    acceleration = models.DecimalField(verbose_name=_('Acceleration'), help_text=_(
        'Rate at which the unit is able to accelerate.'), max_digits=20, decimal_places=10, default=0)
    brake_rate = models.DecimalField(verbose_name=_('Brake rate'), help_text=_(
        'Rate at which the unit is able to decelerate.'), max_digits=20, decimal_places=10, default=0)
    turn_rate = models.IntegerField(verbose_name=_(
        'Turn rate'), help_text=_('Turn rate in binary degree fractions per second (16384 = 360 degrees).'))
    maneuver_leash_length = models.IntegerField(verbose_name=_('Maneuver leash length'), help_text=_(
        'How far a unit will move away from its stationary position in manuver mode.'))

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = _('Unit movement')
        verbose_name_plural = _('Unit movements')
        ordering = ('-game_version', 'unit')
        unique_together = ('game_version', 'unit')
