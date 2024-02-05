# How to Install

- Install and setup odoo 
  - (Mac). https://ajscript.com/odoo/theme/how-to-install-odoo-on-mac-os/
  - Or follow Odoo's official documentation: https://www.odoo.com/documentation/15.0/administration/install/source.html
- Open a new terminal.
- Go to your working directory.
  ```
  $ cd /Users/your_user/Documents/your/working/directory
  ```
- Clone this repository.
  ```
  $ git clone https://github.com/CarlosRamirezT/esd-odoo.git
  ```
- Add the repository path to the addons_path in your config file along with odoo base models. ```/Users/youruser/your/working/directory/odoo-15.conf```
  ```
  addons_path = /Users/your_user/Documents/your/working/directory/odoo/addons,/Users/your_user/Documents/your/working/directory/odoo/odoo/addons,/Users/your_user/Documents/your/working/directory/esd-odoo
  ```
- Add the repository path to the addons_path in your config file along with odoo base models. ```/Users/youruser/your/working/directory/odoo-15.conf````
  ```
  addons_path = /Users/your_user/Documents/your/working/directory/odoo/addons,/Users/your_user/Documents/your/working/directory/odoo/odoo/addons,/Users/your_user/Documents/your/working/directory/esd-odoo
  ````
- Install the module.
  - Install using CLI.
    ```
      $ python odoo-bin -d name-of-db -i health_appointments
    ```
  - Install from the Apps Portal in Odoo.
    - Sign in to your database.
    - Go to Apps.
    - Search for ```Health Appointments```
    - Click Install.
      
    ![img18.png](src%2Fimages%2Fmanifest_images%2Fimg18.png)

# Health Appointments Manager

# Manage User Permissions.
    
    Restrict who can create or edit sensible data in your hospital by setting
    users as Health Appointments Manager or User.
      
Settings > Users & Companies > Users

![img_1.png](src%2Fimages%2Fmanifest_images%2Fimg_1.png)

# Doctor Specialties.
    
    Manage the different specialty areas within your hospital and
    identify your doctors with them.
      
Health Appointments > Doctors > Doctor's Specialties

![img_3.png](src%2Fimages%2Fmanifest_images%2Fimg_3.png)

# Doctors
    
    Manage the different doctors within your hospital and 
    their personal and professional information.
      
Health Appointments > Doctors > Doctors

- View all your doctors.

![img_5.png](src%2Fimages%2Fmanifest_images%2Fimg_5.png)

- Create or Edit your doctor's information.
  - Configure their working schedule for appointments.

![img_7.png](src%2Fimages%2Fmanifest_images%2Fimg_7.png)

# Patients
    
    Manage all your patients in a single place.
      
Health Appointments > Patients > Patients

- View all your patients.

![img_10.png](src%2Fimages%2Fmanifest_images%2Fimg_10.png)

- Create or Edit your patient's information.

![img_11.png](src%2Fimages%2Fmanifest_images%2Fimg_11.png)

- Track their clinical history in a single place.

![img_12.png](src%2Fimages%2Fmanifest_images%2Fimg_12.png)

# Appointments
    
    Manage and schedule appointments for your patients with your
    doctors.
      
Health Appointments > Patients > Appointments

- View all your appointments.

![img_14.png](src%2Fimages%2Fmanifest_images%2Fimg_14.png)

- Create or Edit your appointment's information.

![img_15.png](src%2Fimages%2Fmanifest_images%2Fimg_15.png)

- If the doctor is not working, the system will let you know.

![img_16.png](src%2Fimages%2Fmanifest_images%2Fimg_16.png)

- The system prevents one doctor from having two appointments at the same time.

![img_17.png](src%2Fimages%2Fmanifest_images%2Fimg_17.png)