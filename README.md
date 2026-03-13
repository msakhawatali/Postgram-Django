# Postgram 📸

A full-stack social media web application built with Django — allowing users to share photos, post quotes, like content, and manage their profiles.

---

## 🖥️ Live Demo
👉 [https://postgram1.pythonanywhere.com](https://postgram1.pythonanywhere.com)

---

## ✨ Features

- 🔐 User Authentication — Signup, Login, Logout
- 👤 User Profiles — Profile picture, bio, address, phone number
- 📸 Image Posts — Upload and share photos publicly or privately
- ✍️ Text/Quote Posts — Share thoughts and quotes
- ❤️ Like System — Like and unlike posts
- 🔍 Search — Search posts by username, tags, or description
- 🔒 Privacy Control — Set posts as public or private
- 🔑 Change Password — Secure password update

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap 5 |
| Database | SQLite |
| Auth | Django Auth (Session based) |

---

## 📁 Project Structure

```
Postgram/
│
├── Postgram/          # Main project settings
├── authentication/    # Login, Signup, Logout
├── main/              # Homepage, Feed, Search, Likes
├── user_profile/      # Profile, Posts, Password change
├── templates/         # Base templates
└── static/            # CSS, Images
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/msakhawatali/Postgram-Django.git
cd Postgram-Django
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

### 3. Install requirements.txt
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create superuser (admin)
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

Open your browser and go to: `http://127.0.0.1:8000`

---

## 📸 Screenshots

| Home Page | Profile Page |
|-----------|-------------|
| ![Login Page](screenshots/login.png) | ![Signup Page](screenshots/signup.png) |
| ![Login Page](screenshots/home.png) | ![Login Page](screenshots/single_post.png) |
| ![Login Page](screenshots/profile.png) | ![Login Page](screenshots/profile_update.png) |
| ![Login Page](screenshots/services.png) | ![Signup Page](screenshots/about.png) |
| ![Login Page](screenshots/contact.png) | ![Signup Page](screenshots/change_password.png) |
| ![Login Page](screenshots/post_image.png) | ![Login Page](screenshots/qoutes_post.png) |

---

## 🔮 Future Improvements

- [ ] Follow / Unfollow system
- [ ] Comments on posts
- [ ] Notifications
- [ ] Direct Messages
- [ ] Deploy to production server

---

## 👨‍💻 Author

**Sakhawat Ali**
- GitHub: [@msakhawatali](https://github.com/msakhawatali)
- LinkedIn: [@sakhawat_ali](https://www.linkedin.com/in/sakhawat-ali-dev/)
- Email: msakhawatali131@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
