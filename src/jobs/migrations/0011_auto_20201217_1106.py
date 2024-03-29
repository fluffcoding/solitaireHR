# Generated by Django 3.1.2 on 2020-12-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20201217_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='career_level',
            field=models.CharField(choices=[('Intermediate', 'Intermediate'), ('Experienced Professional', 'Experienced Professional'), ('Entry Level', 'Entry Level'), ('Department Head', 'Department Head'), ('GM / CEO / Country Head', 'GM / CEO / Country Head')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='city',
            field=models.CharField(choices=[('Karachi', 'Karachi'), ('Lahore', 'Lahore'), ('Sialkot City', 'Sialkot City'), ('Faisalabad', 'Faisalabad'), ('Rawalpindi', 'Rawalpindi'), ('Peshawar', 'Peshawar'), ('Saidu Sharif', 'Saidu Sharif'), ('Multan', 'Multan'), ('Gujranwala', 'Gujranwala'), ('Islamabad', 'Islamabad'), ('Quetta', 'Quetta'), ('Bahawalpur', 'Bahawalpur'), ('Sargodha', 'Sargodha'), ('New Mirpur', 'New Mirpur'), ('Chiniot', 'Chiniot'), ('Sukkur', 'Sukkur'), ('Larkana', 'Larkana'), ('Shekhupura', 'Shekhupura'), ('Jhang City', 'Jhang City'), ('Rahimyar Khan', 'Rahimyar Khan'), ('Gujrat', 'Gujrat'), ('Kasur', 'Kasur'), ('Mardan', 'Mardan'), ('Mingaora', 'Mingaora'), ('Dera Ghazi Khan', 'Dera Ghazi Khan'), ('Nawabshah', 'Nawabshah'), ('Sahiwal', 'Sahiwal'), ('Mirpur Khas', 'Mirpur Khas'), ('Okara', 'Okara'), ('Mandi Burewala', 'Mandi Burewala'), ('Jacobabad', 'Jacobabad'), ('Saddiqabad', 'Saddiqabad'), ('Kohat', 'Kohat'), ('Muridke', 'Muridke'), ('Muzaffargarh', 'Muzaffargarh'), ('Khanpur', 'Khanpur'), ('Gojra', 'Gojra'), ('Mandi Bahauddin', 'Mandi Bahauddin'), ('Abbottabad', 'Abbottabad'), ('Dadu', 'Dadu'), ('Khuzdar', 'Khuzdar'), ('Pakpattan', 'Pakpattan'), ('Tando Allahyar', 'Tando Allahyar'), ('Vihari', 'Vihari'), ('Jaranwala', 'Jaranwala'), ('Kamalia', 'Kamalia'), ('Kot Addu', 'Kot Addu'), ('Nowshera', 'Nowshera'), ('Swabi', 'Swabi'), ('Dera Ismail Khan', 'Dera Ismail Khan'), ('Chaman', 'Chaman'), ('Charsadda', 'Charsadda'), ('Kandhkot', 'Kandhkot'), ('Hasilpur', 'Hasilpur'), ('Muzaffarabad', 'Muzaffarabad'), ('Mianwali', 'Mianwali'), ('Jalalpur Jattan', 'Jalalpur Jattan'), ('Bhakkar', 'Bhakkar'), ('Zhob', 'Zhob'), ('Kharian', 'Kharian'), ('Mian Channun', 'Mian Channun'), ('Jamshoro', 'Jamshoro'), ('Pattoki', 'Pattoki'), ('Harunabad', 'Harunabad'), ('Toba Tek Singh', 'Toba Tek Singh'), ('Shakargarh', 'Shakargarh'), ('Hujra Shah Muqim', 'Hujra Shah Muqim'), ('Kabirwala', 'Kabirwala'), ('Mansehra', 'Mansehra'), ('Lala Musa', 'Lala Musa'), ('Nankana Sahib', 'Nankana Sahib'), ('Bannu', 'Bannu'), ('Timargara', 'Timargara'), ('Parachinar', 'Parachinar'), ('Gwadar', 'Gwadar'), ('Abdul Hakim', 'Abdul Hakim'), ('Hassan Abdal', 'Hassan Abdal'), ('Tank', 'Tank'), ('Hangu', 'Hangu'), ('Risalpur Cantonment', 'Risalpur Cantonment'), ('Karak', 'Karak'), ('Kundian', 'Kundian'), ('Umarkot', 'Umarkot'), ('Chitral', 'Chitral'), ('Dainyor', 'Dainyor'), ('Kulachi', 'Kulachi'), ('Kotli', 'Kotli'), ('Gilgit', 'Gilgit'), ('Hyderabad City', 'Hyderabad City'), ('Narowal', 'Narowal'), ('Khairpur Mir’s', 'Khairpur Mir’s'), ('Khanewal', 'Khanewal'), ('Jhelum', 'Jhelum'), ('Haripur', 'Haripur'), ('Shikarpur', 'Shikarpur'), ('Rawala Kot', 'Rawala Kot'), ('Hafizabad', 'Hafizabad'), ('Lodhran', 'Lodhran'), ('Malakand', 'Malakand'), ('Attock City', 'Attock City'), ('Batgram', 'Batgram'), ('Matiari', 'Matiari'), ('Ghotki', 'Ghotki'), ('Naushahro Firoz', 'Naushahro Firoz'), ('Alpurai', 'Alpurai'), ('Bagh', 'Bagh'), ('Daggar', 'Daggar'), ('Bahawalnagar', 'Bahawalnagar'), ('Leiah', 'Leiah'), ('Tando Muhammad Khan', 'Tando Muhammad Khan'), ('Chakwal', 'Chakwal'), ('Khushab', 'Khushab'), ('Badin', 'Badin'), ('Lakki', 'Lakki'), ('Rajanpur', 'Rajanpur'), ('Dera Allahyar', 'Dera Allahyar'), ('Shahdad Kot', 'Shahdad Kot'), ('Pishin', 'Pishin'), ('Sanghar', 'Sanghar'), ('Upper Dir', 'Upper Dir'), ('Thatta', 'Thatta'), ('Dera Murad Jamali', 'Dera Murad Jamali'), ('Kohlu', 'Kohlu'), ('Mastung', 'Mastung'), ('Dasu', 'Dasu'), ('Athmuqam', 'Athmuqam'), ('Loralai', 'Loralai'), ('Barkhan', 'Barkhan'), ('Musa Khel Bazar', 'Musa Khel Bazar'), ('Ziarat', 'Ziarat'), ('Gandava', 'Gandava'), ('Sibi', 'Sibi'), ('Dera Bugti', 'Dera Bugti'), ('Eidgah', 'Eidgah'), ('Turbat', 'Turbat'), ('Uthal', 'Uthal'), ('Khuzdar', 'Khuzdar'), ('Chilas', 'Chilas'), ('Kalat', 'Kalat'), ('Panjgur', 'Panjgur'), ('Gakuch', 'Gakuch'), ('Qila Saifullah', 'Qila Saifullah'), ('Kharan', 'Kharan'), ('Aliabad', 'Aliabad'), ('Awaran', 'Awaran'), ('Dalbandin', 'Dalbandin')], max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(blank=True, choices=[('1 years', '1 years'), ('2 years', '2 years'), ('3 years', '3 years'), ('4 years', '4 years'), ('5 years', '5 years'), ('6 years', '6 years'), ('7 years', '7 years'), ('8 years', '8 years'), ('9 years', '9 years'), ('10 years', '10 years'), ('11 years', '11 years'), ('12 years', '12 years'), ('13 years', '13 years'), ('14 years', '14 years'), ('15 years', '15 years'), ('16 years', '16 years'), ('17 years', '17 years'), ('18 years', '18 years'), ('19 years', '19 years'), ('20 years', '20 years'), ('21 years', '21 years'), ('22 years', '22 years'), ('23 years', '23 years'), ('24 years', '24 years'), ('25 years', '25 years'), ('26 years', '26 years'), ('27 years', '27 years'), ('28 years', '28 years'), ('29 years', '29 years'), ('30 years', '30 years'), ('31 years', '31 years'), ('32 years', '32 years'), ('33 years', '33 years'), ('34 years', '34 years'), ('35 years', '35 years')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='gender',
            field=models.CharField(blank=True, choices=[('No preference', 'No preference'), ('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_shift',
            field=models.CharField(choices=[('All', 'All'), ('Morning', 'Morning'), ('Evening', 'Evening'), ('Night', 'Night')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Internship', 'Internship'), ('Freelancing', 'Freelancing'), ('Contract', 'Contract'), ('Full time', 'Full time'), ('Part time', 'Part time'), ('Permanent', 'Permanent')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='max_salary',
            field=models.CharField(blank=True, choices=[(0, 0), (5000, 5000), (10000, 10000), (15000, 15000), (20000, 20000), (25000, 25000), (30000, 30000), (35000, 35000), (40000, 40000), (45000, 45000), (50000, 50000), (55000, 55000), (60000, 60000), (65000, 65000), (70000, 70000), (75000, 75000), (80000, 80000), (85000, 85000), (90000, 90000), (95000, 95000), (100000, 100000), (105000, 105000), (110000, 110000), (115000, 115000), (120000, 120000), (125000, 125000), (130000, 130000), (135000, 135000), (140000, 140000), (145000, 145000), (150000, 150000), (155000, 155000), (160000, 160000), (165000, 165000), (170000, 170000), (175000, 175000), (180000, 180000), (185000, 185000), (190000, 190000), (195000, 195000), (200000, 200000), (205000, 205000), (210000, 210000), (215000, 215000), (220000, 220000), (225000, 225000), (230000, 230000), (235000, 235000), (240000, 240000), (245000, 245000)], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='minimum_salary',
            field=models.CharField(blank=True, choices=[(0, 0), (5000, 5000), (10000, 10000), (15000, 15000), (20000, 20000), (25000, 25000), (30000, 30000), (35000, 35000), (40000, 40000), (45000, 45000), (50000, 50000), (55000, 55000), (60000, 60000), (65000, 65000), (70000, 70000), (75000, 75000), (80000, 80000), (85000, 85000), (90000, 90000), (95000, 95000), (100000, 100000), (105000, 105000), (110000, 110000), (115000, 115000), (120000, 120000), (125000, 125000), (130000, 130000), (135000, 135000), (140000, 140000), (145000, 145000), (150000, 150000), (155000, 155000), (160000, 160000), (165000, 165000), (170000, 170000), (175000, 175000), (180000, 180000), (185000, 185000), (190000, 190000), (195000, 195000), (200000, 200000), (205000, 205000), (210000, 210000), (215000, 215000), (220000, 220000), (225000, 225000), (230000, 230000), (235000, 235000), (240000, 240000), (245000, 245000)], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='expected_salary_maximum',
            field=models.CharField(choices=[(0, 0), (5000, 5000), (10000, 10000), (15000, 15000), (20000, 20000), (25000, 25000), (30000, 30000), (35000, 35000), (40000, 40000), (45000, 45000), (50000, 50000), (55000, 55000), (60000, 60000), (65000, 65000), (70000, 70000), (75000, 75000), (80000, 80000), (85000, 85000), (90000, 90000), (95000, 95000), (100000, 100000), (105000, 105000), (110000, 110000), (115000, 115000), (120000, 120000), (125000, 125000), (130000, 130000), (135000, 135000), (140000, 140000), (145000, 145000), (150000, 150000), (155000, 155000), (160000, 160000), (165000, 165000), (170000, 170000), (175000, 175000), (180000, 180000), (185000, 185000), (190000, 190000), (195000, 195000), (200000, 200000), (205000, 205000), (210000, 210000), (215000, 215000), (220000, 220000), (225000, 225000), (230000, 230000), (235000, 235000), (240000, 240000), (245000, 245000)], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='expected_salary_minimum',
            field=models.CharField(choices=[(0, 0), (5000, 5000), (10000, 10000), (15000, 15000), (20000, 20000), (25000, 25000), (30000, 30000), (35000, 35000), (40000, 40000), (45000, 45000), (50000, 50000), (55000, 55000), (60000, 60000), (65000, 65000), (70000, 70000), (75000, 75000), (80000, 80000), (85000, 85000), (90000, 90000), (95000, 95000), (100000, 100000), (105000, 105000), (110000, 110000), (115000, 115000), (120000, 120000), (125000, 125000), (130000, 130000), (135000, 135000), (140000, 140000), (145000, 145000), (150000, 150000), (155000, 155000), (160000, 160000), (165000, 165000), (170000, 170000), (175000, 175000), (180000, 180000), (185000, 185000), (190000, 190000), (195000, 195000), (200000, 200000), (205000, 205000), (210000, 210000), (215000, 215000), (220000, 220000), (225000, 225000), (230000, 230000), (235000, 235000), (240000, 240000), (245000, 245000)], max_length=50),
        ),
    ]
