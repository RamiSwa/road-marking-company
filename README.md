# 🚧 Road Marking Company – Bilingual Corporate Website 🌍

**Road Marking Company** is a fully dynamic, SEO-optimized, bilingual (English/Hebrew) corporate website built with Django. It includes RTL/LTR layout support, admin-driven content, and a clean, modern UI — designed for infrastructure companies offering road marking, signage, and related services.

---

## 📸 Preview

![road-marking-company-1](https://github.com/user-attachments/assets/6e30bbea-7cda-4fd7-938b-09f2825097ef)

🔗 **Live Demo**: [road-marking-company-production.up.railway.app](https://road-marking-company-production.up.railway.app)

---

## 🚀 Key Features

- 🌐 **Bilingual Support** – English & Hebrew (with `gettext_lazy` + Django ModelTranslation)
- 📐 **RTL/LTR Switching** – Auto layout direction per language
- 📥 **Contact Form** – Email-integrated, stored in DB
- 🖼️ **Dynamic Project Gallery** – Multi-image upload per project
- 🧩 **Modular Architecture** – 7 Django apps: `core`, `about`, `services`, `projects`, `blog`, `store`, `contacts`
- 🛠️ **Admin-Driven Content** – Everything managed via Django Admin
- 🔍 **SEO Ready** – Custom slugs, meta tags, Open Graph support
- 🐳 **Dockerized** – Redis + PostgreSQL + Celery-ready

---

## 🧠 Tech Stack

| Category         | Technologies                                         |
|------------------|-----------------------------------------------------|
| **Backend**      | Django, PostgreSQL, Redis, Celery                   |
| **Frontend**     | Bootstrap 5, custom CSS with full RTL support       |
| **DevOps**       | Docker, Railway, Cloudflare, GitHub Actions         |
| **Media/Storage**| R2 via Cloudflare                                   |
| **SEO & Speed**  | Sitemap, Open Graph, lazy loading, compressed assets|

---

## 🧪 App Structure

| App        | Purpose                                                    |
|------------|------------------------------------------------------------|
| `core`     | Global settings, SEO tags, logo, footer, contact info      |
| `about`    | Company mission, values, and profile                       |
| `services` | Road marking & infrastructure service listings             |
| `projects` | Dynamic gallery showcasing past work with multiple images  |
| `blog`     | SEO-ready content system (prepared for future posts)       |
| `store`    | Product catalog for signage, safety gear, etc.             |
| `contacts` | Contact form with email notifications and storage          |

---

## 🎨 Visual Design

- 💡 Hero sections with overlays & call-to-actions
- 🖼️ Interactive project gallery
- 🪄 RTL support through dynamic template logic
- 📱 Fully responsive and mobile-optimized
- 🎯 Clean, modern, business-first UI

---

## 🧩 Built For Growth

- 🔁 **Modular & Maintainable** – 7 apps with clear roles
- 🌐 **Internationalization** – Ready for multilingual expansion
- 📈 **Scalable Stack** – PostgreSQL, Redis, Docker, Celery
- 🧑‍💻 **No Hardcoding** – All content editable in admin

---

## 🐳 Local Setup (Docker)

```bash
git clone https://github.com/yourusername/road-marking-company.git
cd road-marking-company
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
pip install -r requirements.txt

docker-compose up --build



⚙️ Environment Variables (.env example)
```env
# ✅ PostgreSQL
POSTGRES_USER=
POSTGRES_PASSWORD=
PGHOST=
PGPORT=
POSTGRES_DB=
DATABASE_URL=

# ✅ Redis
REDIS_URL=
CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=
REDISHOST=
REDISPORT=
REDISUSER=
REDIS_PASSWORD=

# ✅ Django
DEBUG=True
SECRET_KEY=
ALLOWED_HOSTS=

# ✅ Cloudflare R2
R2_ACCESS_KEY_ID=
R2_SECRET_ACCESS_KEY=
R2_BUCKET_NAME=
R2_ENDPOINT_URL=
R2_CUSTOM_DOMAIN=

# ✅ Email
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

```

📬 Contact
Need a custom website for your business?

🌐 Portfolio: impactbyrami.com

📫 Email: rami@impactbyrami.com

