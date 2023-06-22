from django.db import models
from django.conf import settings
from django.contrib.auth.models import UserManager,AbstractBaseUser, PermissionsMixin
from localflavor.us.models import USStateField
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class CustomeUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('You have not provided a valid email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)





class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomeUserManager()

    USERNAME_FIELD: str = 'email'
    EMAIL_FIELD: str = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural= 'Users'


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.last_name

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(('LDH Region must be 1-9!'))

class Event(models.Model):
    PARISH_CHOICES = [
        ('Acadia', 'Acadia'),
        ('Allen', 'Allen'),
        ('Ascension', 'Ascension'),
        ('Assumption', 'Assumption'),
        ('Avoyelles', 'Avoyelles'),
        ('Beauregard', 'Beauregard'),
        ('Bienville', 'Bienville'),
        ('Bossier', 'Bossier'),
        ('Caddo', 'Caddo'),
        ('Calcasieu', 'Calcasieu'),
        ('Caldwell', 'Caldwell'),
        ('Cameron', 'Cameron'),
        ('Catahoula', 'Catahoula'),
        ('Claiborne', 'Claiborne'),
        ('Concordia', 'Concordia'),
        ('De Soto', 'De Soto'),
        ('East Baton Rouge', 'East Baton Rouge'),
        ('East Carroll', 'East Carroll'),
        ('East Feliciana', 'East Feliciana'),
        ('Evangeline', 'Evangeline'),
        ('Franklin', 'Franklin'),
        ('Grant', 'Grant'),
        ('Iberia', 'Iberia'),
        ('Iberville', 'Iberville'),
        ('Jackson', 'Jackson'),
        ('Jefferson', 'Jefferson'),
        ('Jefferson Davis', 'Jefferson Davis'),
        ('Lafayette', 'Lafayette'),
        ('Lafourche', 'Lafourche'),
        ('LaSalle', 'LaSalle'),
        ('Lincoln', 'Lincoln'),
        ('Livingston', 'Livingston'),
        ('Madison', 'Madison'),
        ('Morehouse', 'Morehouse'),
        ('Natchitoches', 'Natchitoches'),
        ('Orleans', 'Orleans'),
        ('Ouachita', 'Ouachita'),
        ('Plaquemines', 'Plaquemines'),
        ('Pointe Coupee', 'Pointe Coupee'),
        ('Rapides', 'Rapides'),
        ('Red River', 'Red River'),
        ('Richland', 'Richland'),
        ('Sabine', 'Sabine'),
        ('St. Bernard', 'St. Bernard'),
        ('St. Charles', 'St. Charles'),
        ('St. Helena', 'St. Helena'),
        ('St. James', 'St. James'),
        ('St. John the Baptist', 'St. John the Baptist'),
        ('St. Landry', 'St. Landry'),
        ('St. Martin', 'St. Martin'),
        ('St. Mary', 'St. Mary'),
        ('St. Tammany', 'St. Tammany'),
        ('Tangipahoa', 'Tangipahoa'),
        ('Tensas', 'Tensas'),
        ('Terrebonne', 'Terrebonne'),
        ('Union', 'Union'),
        ('Vermilion', 'Vermilion'),
        ('Vernon', 'Vernon'),
        ('Washington', 'Washington'),
        ('Webster', 'Webster'),
        ('West Baton Rouge', 'West Baton Rouge'),
        ('West Carroll', 'West Carroll'),
        ('West Feliciana', 'West Feliciana'),
        ('Winn', 'Winn')
        ]

    # Fields of the Event model
    date = models.DateField()
    code = models.CharField(max_length=9, validators=[MinLengthValidator(9, message='Code must be exactly nine digits')])
    region = models.CharField(max_length=9, validators=[validate_nonzero])
    parish = models.CharField(max_length=50, choices=PARISH_CHOICES)
    city = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    approval_from_RMD = models.CharField(max_length=3, choices=(("yes", "Yes"), ("no", "No")), null=True)
    vaccines_offered = models.CharField(max_length=5, choices=(("COVID", "COVID"), ("FLU", "FLU"), ("M POX", "M POX")), null=True)
    status = models.CharField(max_length=9, choices=(("complete", "Complete"), ("working", "Working"), ("cancelled", "Cancelled")), null=True)
    num_of_doses = models.PositiveIntegerField(null=True)
    num_of_doses_administered = models.PositiveIntegerField(null=True)
    patient_edu_res_brought = models.PositiveIntegerField(null=True)
    patient_edu_res_distributed = models.PositiveIntegerField(null=True)


    def __str__(self):
        return self.parish



# class Airport(models.Model):
#     code = models.CharField(max_length=50)
#     city = models.CharField(max_length=100)
#     state = USStateField()

#     def __str__(self) -> str:
#         return f"{self.code}"

# class Airline(models.Model):
#     code = models.CharField(max_length=50)
#     name = models.CharField(max_length=100)

#     def __str__(self) -> str:
#         return f"{self.code}"



# class Day(models.Model):

#     class Weekday(models.TextChoices):
#         mon = "Mon", "Monday"
#         tue = "Tue", "Tuesday"
#         wed = "Wed", "Wednesday"
#         thu = "Thu", "Thursday"
#         fri = "Fri", "Friday"
#         sat = "Sat", "Saturday"
#         sun = "Sun", "Sunday"
#     day = models.CharField(max_length=3, choices= Weekday.choices)

#     def __str__(self) -> str:
#         return self.get_day_display()

# class flightClass(models.Model):
#     class_name = models.CharField(max_length=50)
#     def __str__(self) -> str:
#         return self.class_name




# class Flight(models.Model):
#     flight_id = models.AutoField(primary_key=True)
#     flight_num = models.BigIntegerField()
#     airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
#     origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flight_origin")
#     destin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flight_destin")
#     days_of_week = models.ManyToManyField(Day)
#     seats = models.IntegerField(default=0)

#     def __str__(self) -> str:
#         return f"{self.flight_id}: {self.airline} {self.flight_num} || {self.origin} --> {self.destin}"



# class Route(models.Model):
#     flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     segment = models.IntegerField(default=0)
#     origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="route_origin")
#     destin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="route_destin")
#     departure_time = models.TimeField()
#     duration = models.DurationField()

#     def __str__(self) -> str:
#         return f"{self.flight_id}-{self.segment}"

# class Price(models.Model):
#     # class Classes(models.TextChoices):
#     #     eco = "Eco", "Economy"
#     #     bus = "Bus", "Bussiness"
#     #     frt = "Frt", "First"

#     flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     # flight_class = models.CharField(max_length=50, choices=Classes.choices)
#     flight_class = models.ForeignKey(flightClass, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=6, decimal_places=2, default = 0.00)

#     def __str__(self) -> str:
#         # return f"{self.flight_id} - {self.get_flight_class_display()}"
#         return f"{self.flight_id} - {self.flight_class}"

# # class User(models.Model):

# #     user_id = models.AutoField(primary_key=True)
# #     fname = models.CharField(max_length=50)
# #     lname = models.CharField(max_length=50)
# #     address = models.CharField(max_length=200)
# #     city = models.CharField(max_length=50)
# #     state = USStateField()
# #     email = models.EmailField(max_length=100)
# #     phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)])


# #     def __str__(self) -> str:
# #         return f"{self.fname} {self.lname}"


# class Reservation(models.Model):

#     reservation_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     fl_class = models.ForeignKey(flightClass, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return f"{self.reservation_id} - {self.user}"







