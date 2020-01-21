from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.validity=False
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
    year_of_passing         = (('2021','2021'),('2020','2020'),('2019','2019'),('2018','2018'),('2017','2017'))
    field_of_study=[('Engineering','Engineering'),('Arts','Arts'),('Science','Science'),('Nursery','Nursery'),('Doctor','Doctor')]
    college_choice=(('Government College of Arts, Science and Commerce, Khandola, Marcela Goa','Government College of Arts, Science and Commerce, Khandola, Marcela Goa'),
    ('Government College of Arts, Science & Commerce, Sanquelim-Goa','Government College of Arts, Science & Commerce, Sanquelim-Goa'),
	('Government College of Arts, Science & Commerce, Quepem-Goa','Government College of Arts, Science & Commerce, Quepem-Goa'),
	('Sant Sohirobanath Ambiye Government College of Arts & Commerce, VIrnoda-Pernem, Goa.','Sant Sohirobanath Ambiye Government College of Arts & Commerce, VIrnoda-Pernem, Goa.'),
	('Government College of Commerce & Economics, Borda-Margao, Goa','Government College of Commerce & Economics, Borda-Margao, Goa'),
	('Goa College of Music, Kala Academys Complex, Campal, Panaji-Goa.','Goa College of Music, Kala Academys Complex, Campal, Panaji-Goa.'),
	('Goa College of Home Science, Campal, Panaji, Goa','Goa College of Home Science, Campal, Panaji, Goa'),
	('II. Non-Government Aided Colleges','II. Non-Government Aided Colleges'),
	('Shree Mallikarjun College of Arts & Commerce, Canacona Goa','Shree Mallikarjun College of Arts & Commerce, Canacona Goa'),
	('Nirmala Institute of Education, Altinho Panaji, Goa','Nirmala Institute of Education, Altinho Panaji, Goa'),
	('Dhempe College of Arts & Science, Panaji, Goa.','Dhempe College of Arts & Science, Panaji, Goa.'),
	('V.M. Salgaocar College of law, Miramar, Panaji Goa','V.M. Salgaocar College of law, Miramar, Panaji Goa'),
	('S.S. Dempo College of Commerce & Economics, Altinho, Panaji, Goa','S.S. Dempo College of Commerce & Economics, Altinho, Panaji, Goa'),
	('College of Commerce and Economics, Ponda Goa','College of Commerce and Economics, Ponda Goa'),
	('Carmel College of Arts, Science & Commerce for Women, Nuvem Goa','Carmel College of Arts, Science & Commerce for Women, Nuvem Goa'),
	)
    college=models.CharField(max_length=200,choices=college_choice,default='Government College of Arts, Science and Commerce, Khandola, Marcela Goa')
    occupation_type=[('home-maker','home-maker'),('Entreprenuer','Entreprenuer'),('Employed','Employed')]
    occupation=models.CharField(max_length=100,choices=occupation_type,default="Employed")
    field=models.CharField(max_length=100,choices=field_of_study,default="Engineering")
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    username 				= models.CharField(max_length=30, unique=True)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    year = models.CharField(max_length=10, choices=year_of_passing)
    validity=models.BooleanField(default=False)
    register_number         = models.IntegerField(default=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()

    def __str__(self):
        return self.email+" "+self.username+" "+self.year+" "+self.field+" "+self.occupation

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

class colleges(models.Model):
	college_code=models.CharField(max_length=100,primary_key=True)
	password=models.CharField(max_length=100)
	college_name=models.CharField(max_length=200)

	def __str__(self):
		return self.college_code