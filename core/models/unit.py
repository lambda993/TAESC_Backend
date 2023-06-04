from core.utils.models import CoreModel
from django.db import models
from django.core.validators import RegexValidator
from .category import UnitCategory
from .tedclass import TEDClass
from .side import UnitSide


class Unit(CoreModel):
    unit_name = models.CharField(
        max_length=20, help_text="Unit ingame ID code")
    unit_number = models.IntegerField(help_text="Ingame unit ID")
    commander = models.BooleanField(
        default=False, help_text="If game ends ruleset is selected, the death of this unit will end the game")
    show_player_name = models.BooleanField(
        default=False, help_text="Player's name will replace this unit's name")
    name = models.CharField(max_length=50)
    german_name = models.CharField(max_length=50, blank=True)
    french_name = models.CharField(max_length=50, blank=True)
    spanish_name = models.CharField(max_length=50, blank=True)
    italian_name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100)
    german_description = models.CharField(max_length=100, blank=True)
    french_description = models.CharField(max_length=100, blank=True)
    spanish_description = models.CharField(max_length=100, blank=True)
    italian_description = models.CharField(max_length=100, blank=True)
    side = models.ForeignKey(
        UnitSide, on_delete=models.PROTECT, related_name="unit_side")
    designation = models.CharField(
        max_length=20, blank=True, help_text="Unit 3D model name")
    footprint = models.CharField(max_length=10, validators=[RegexValidator(
        regex=r"^\d{1,2}x\d{1,2}$", message="Footprint must be of the AAxAA or AxA (where A is a digit) format!")])
    yard_map = models.CharField(
        max_length=500, blank=True, help_text="Map of how the game engine handles collisions")
    build_energy_cost = models.IntegerField()
    build_metal_cost = models.IntegerField()
    build_time_cost = models.IntegerField()
    energy_use = models.DecimalField(
        max_digits=20, decimal_places=10, default=0)
    metal_use = models.DecimalField(
        max_digits=20, decimal_places=10, default=0)
    energy_make = models.DecimalField(
        max_digits=20, decimal_places=10, default=0)
    metal_make = models.DecimalField(
        max_digits=20, decimal_places=10, default=0)
    energy_store = models.IntegerField(default=0)
    metal_store = models.IntegerField(default=0)
    max_damage = models.IntegerField(help_text="Unit health points")
    damage_modifier = models.DecimalField(
        max_digits=20, decimal_places=10, default=1, help_text="Damage reduction that is applied to the unit when hit by any damage")
    heal_time = models.IntegerField(null=True, blank=True, default=0)
    hide_damage = models.BooleanField(
        default=False, help_text="Unit health bar is not displayed")
    immune_to_paralyze = models.BooleanField(
        default=False, help_text="This unit is immune to stun weapons")
    sight_distance = models.IntegerField()
    radar_distance = models.IntegerField(null=True, blank=True)
    radar_jammer = models.IntegerField(null=True, blank=True)
    sonar_distance = models.IntegerField(null=True, blank=True)
    sonar_jammer = models.IntegerField(null=True, blank=True)
    stealth = models.BooleanField(
        default=False, help_text="This unit is invisible on the map")
    category = models.ManyToManyField(
        UnitCategory, related_name="unit_category")
    bad_target_category = models.ForeignKey(
        UnitCategory, on_delete=models.PROTECT, related_name="unit_bad_target_category", null=True, blank=True)
    no_chase_category = models.ForeignKey(
        UnitCategory, on_delete=models.PROTECT, related_name="unit_no_chase_category", null=True, blank=True)
    editor_class = models.ForeignKey(
        TEDClass, on_delete=models.PROTECT, related_name="unit_tedclass")
    # sound_category=models.ForeignKey(SoundCategory,on_delete=models.PROTECT,related_name="units")
    # movement_class=models.ForeignKey(MovementClass,on_delete=models.PROTECT,related_name="units")
    # default_orders=models.ForeignKey(UnitOrders,on_delete=models.PROTECT,related_name="units")
    # explode_as=models.ForeignKey(Weapon,on_delete=models.PROTECT,related_name="units")
    # self_destruct_as=models.ForeignKey(Weapon,on_delete=models.PROTECT,related_name="units")
    # corpse=models.ForeignKey(Corpse,on_delete=models.PROTECT,related_name="units")
    self_destruct_countdown = models.SmallIntegerField(
        null=True, blank=True, default=5)
    # weapon1=models.ForeignKey(Weapon,on_delete=models.PROTECT,related_name="units")
    weapon1_bad_target = models.ForeignKey(
        UnitCategory, on_delete=models.PROTECT, related_name="unit_w1_bad_target", null=True, blank=True)
    # weapon2=models.ForeignKey(Weapon,on_delete=models.PROTECT,related_name="units")
    weapon2_bad_target = models.ForeignKey(
        UnitCategory, on_delete=models.PROTECT, related_name="unit_w2_bad_target", null=True, blank=True)
    # weapon3=models.ForeignKey(Weapon,on_delete=models.PROTECT,related_name="units")
    weapon3_bad_target = models.ForeignKey(
        UnitCategory, on_delete=models.PROTECT, related_name="unit_w3_bad_target", null=True, blank=True)
    shoot_me = models.BooleanField(
        default=False, help_text="Unit is engaged automatically when in range")
    antiweapons = models.BooleanField(
        default=False, help_text="This unit has anti-nuke weapons")
    amphibious = models.BooleanField(
        default=False, help_text="This unit can go underwater")
    floater = models.BooleanField(
        default=False, help_text="This unit can be engaged by torpedo weapons")
    digger = models.BooleanField(
        default=False, help_text="This unit is partially undergound")
    can_fly = models.BooleanField(
        default=False, help_text="This unit is immune to ground damage explosions")
    can_hover = models.BooleanField(
        default=False, help_text="This unit hovers over water, cannot be engaged by torpedo weapons")
    is_airbase = models.BooleanField(
        default=False, help_text="Aircraft can land on this unit for repairs")
    is_feature = models.BooleanField(
        default=False, help_text="This unit will become a map feature when built and will not count towards unit limit")
    is_targeting_upgrade = models.BooleanField(
        default=False, help_text="This unit will upgrade commanders and allow autonomous fire on units that are detected by radar/sonar")

    def __str__(self):
        return self.unit_name

    class Meta:
        ordering = ["unit_name", "unit_number"]
