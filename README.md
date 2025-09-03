# PuntoDeVentaCV - Point of Sale System

A **Django-based web application** for small business inventory and sales management. Users can manage products, brands, categories, and suppliers through a secure web interface.

---

## Features

* User authentication with **email-based login**
* CRUD operations for **Products, Brands, Categories, Suppliers**
* Containerized deployment using **Docker**
* Automated CI/CD with **Jenkins**
* Responsive frontend with **Bootstrap & FontAwesome**

---

## Technology Stack

* **Backend:** Django 5.1.3, Python 3.12
* **Database:** MySQL (with `mysqlclient`)
* **Frontend:** Bootstrap 5.3.3, FontAwesome
* **Image Processing:** Pillow 11.0.0
* **Deployment:** Docker Compose, Jenkins CI/CD

---

## Architecture

* **Landing App:** Authentication & account management
* **POS App:** Inventory and sales management
* **Containers:**

  * `django-container` (app) on port 8000
  * `mysql-container` (database) on port 3307:3306
* **Network & Volumes:** `django-network` bridge, `mysql_data` volume for persistence

---

## Deployment

* Automated via **Jenkins pipeline**: checkout → container management → build & deploy → DB setup → migrations → restart services
* Uses **environment variables** for DB config and health checks (`wait-for-it.sh`)

---

## Security

* Custom user model (`Landing.CustomUser`)
* Email-based login, session management, and custom password validation


---
## Documentation
### DeepWiki
- [DeepWiki](https://deepwiki.com/Carlos56g/PIALenguajesModernos)
### Original Documentation (Spanish)
- [Proyect Document](https://drive.google.com/file/d/1FGir_kmVfJ--YY96IUb2Ow4IPE2H4k6_/view?usp=drive_link)
