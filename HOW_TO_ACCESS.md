# 📘 دليل الدخول والتجربة | Access and Try Guide

## كيف أدخل إلى النظام وأجربه؟ | How to Access and Try the System?

هذا الدليل يشرح خطوة بخطوة كيفية الدخول إلى نظام إدارة الطلاب الذكي وتجربة جميع الميزات.

This guide explains step-by-step how to access the Smart Student Management System and try all features.

---

## 📋 الخطوات السريعة | Quick Steps

### الخطوة 1️⃣: تشغيل النظام | Step 1: Start the System

افتح Terminal (نافذة الأوامر) واكتب:
Open Terminal and type:

```bash
cd /home/runner/work/InfoSecNazir/InfoSecNazir
python3 manage.py runserver
```

**ماذا سيحدث:**
- سيبدأ النظام بالعمل
- ستظهر رسالة مثل: "Starting development server at http://127.0.0.1:8000/"
- اترك هذه النافذة مفتوحة

**What will happen:**
- The system will start running
- You'll see a message like: "Starting development server at http://127.0.0.1:8000/"
- Keep this window open

---

### الخطوة 2️⃣: فتح المتصفح | Step 2: Open Browser

افتح متصفح الإنترنت (Chrome, Firefox, Safari, أو أي متصفح)
Open your web browser (Chrome, Firefox, Safari, or any browser)

**اكتب أحد هذه الروابط:**
**Type one of these URLs:**

#### أ) الصفحة الرئيسية | Main Homepage
```
http://127.0.0.1:8000/
أو
http://localhost:8000/
```

#### ب) لوحة الإدارة | Admin Panel
```
http://127.0.0.1:8000/admin/
أو
http://localhost:8000/admin/
```

---

### الخطوة 3️⃣: الدخول إلى لوحة الإدارة | Step 3: Login to Admin

**بيانات الدخول:**
**Login Credentials:**

```
اسم المستخدم | Username: admin
كلمة المرور | Password: admin123
```

**📝 ملاحظة:** احفظ هذه البيانات! ستحتاجها في كل مرة تدخل فيها.
**📝 Note:** Save these credentials! You'll need them every time you login.

---

## 🎯 جولة في النظام | System Tour

### 1. الصفحة الرئيسية | Homepage
**الرابط:** http://localhost:8000/

**ماذا سترى:**
- إحصائيات عامة (عدد الطلاب، الجلسات، السجلات)
- أزرار سريعة للوصول إلى المسح الضوئي ولوحة التحكم
- جدول بآخر الجلسات
- قائمة الميزات المتاحة

**What you'll see:**
- General statistics (students, sessions, records count)
- Quick buttons for scanner and dashboard
- Recent sessions table
- Available features list

---

### 2. لوحة التحكم | Dashboard
**الرابط:** http://localhost:8000/dashboard/

**ماذا ستجد:**
- إحصائيات تفصيلية
- أفضل الطلاب حضوراً
- الطلاب المعرضين للخطر (أقل من 50% حضور)
- تقسيم الجلسات حسب النوع
- آخر سجلات الحضور
- زر تصدير إلى Excel

**What you'll find:**
- Detailed statistics
- Top performing students
- At-risk students (< 50% attendance)
- Session breakdown by type
- Recent attendance logs
- Excel export button

---

### 3. إدارة الطلاب | Student Management
**الرابط:** http://localhost:8000/students/

**ما يمكنك فعله:**
- عرض قائمة جميع الطلاب
- البحث عن طالب (بالاسم أو الرقم الجامعي أو البريد)
- فلترة الطلاب حسب نسبة الحضور
- النقر على طالب لرؤية التفاصيل
- رؤية نسبة الحضور لكل طالب

**What you can do:**
- View all students list
- Search for a student (by name, ID, or email)
- Filter students by attendance percentage
- Click on a student to see details
- View attendance percentage for each student

---

### 4. إدارة الجلسات | Session Management
**الرابط:** http://localhost:8000/sessions/

**ما يمكنك فعله:**
- عرض جميع الجلسات
- فلترة حسب النوع (محاضرة، معمل، امتحان)
- فلترة حسب التاريخ
- النقر على جلسة لرؤية سجل الحضور
- رؤية عدد الحاضرين والغائبين

**What you can do:**
- View all sessions
- Filter by type (lecture, lab, exam)
- Filter by date
- Click on a session to see attendance records
- See present/absent counts

---

### 5. الماسح الضوئي | QR Scanner
**الرابط:** http://localhost:8000/scanner/

**كيف تستخدمه:**
1. اختر جلسة من القائمة
2. اختر حالة الحضور (حاضر، متأخر، غائب)
3. اضغط "Start Scanner" لتشغيل الكاميرا
4. أو أدخل UUID الطالب يدوياً

**How to use it:**
1. Select a session from dropdown
2. Choose attendance status (Present, Late, Absent)
3. Click "Start Scanner" to activate camera
4. Or enter student UUID manually

**📱 ملاحظة:** قد تحتاج للسماح بالوصول إلى الكاميرا في المتصفح
**📱 Note:** You may need to allow camera access in your browser

---

### 6. لوحة الإدارة الكاملة | Full Admin Panel
**الرابط:** http://localhost:8000/admin/

**ما يمكنك فعله:**

#### أ) إدارة الطلاب | Student Management
**المسار:** Admin → Students → Students

**الإجراءات المتاحة:**
- ✅ إضافة طالب جديد (Add Student)
- ✅ تعديل بيانات طالب (Edit)
- ✅ حذف طالب (Delete)
- ✅ توليد رموز QR من جديد (Regenerate QR codes)
- ✅ تصدير قائمة الطلاب

**كيف تضيف طالب جديد:**
```
1. اضغط "Add Student" في الزاوية العليا
2. أدخل:
   - University ID (مثلاً: CS2021006)
   - Name (مثلاً: علي محمود)
   - Email (مثلاً: ali@university.edu)
   - Phone (اختياري)
3. اضغط "Save"
4. سيتم توليد رمز QR تلقائياً!
```

#### ب) إدارة الجلسات | Session Management
**المسار:** Admin → Students → Sessions

**كيف تضيف جلسة جديدة:**
```
1. اضغط "Add Session"
2. أدخل:
   - Title (مثلاً: محاضرة قواعد البيانات)
   - Type (اختر: Lecture, Lab, Exam, etc.)
   - Date (التاريخ)
   - Start time (وقت البدء - اختياري)
   - Location (المكان - مثلاً: قاعة 101)
3. اضغط "Save"
```

#### ج) عرض سجلات الحضور | View Attendance Logs
**المسار:** Admin → Students → Attendance Logs

**ما سترى:**
- قائمة بجميع سجلات الحضور
- الطالب، الجلسة، الحالة، الوقت
- من سجّل الحضور

#### د) الشارات | Badges
**المسار:** Admin → Students → Badges

**الشارات المتاحة حالياً:**
- 🏆 Perfect Attendance (حضور كامل)
- ⏰ Early Bird (الحضور المبكر)
- 📚 Assignment Master (إتمام الواجبات)

---

## 🧪 كيف تجرب النظام | How to Test the System

### تجربة 1: إضافة طالب جديد

```
1. اذهب إلى: http://localhost:8000/admin/
2. سجل الدخول: admin / admin123
3. اضغط على "Students" في قسم "Students"
4. اضغط "Add Student" (أزرق في الزاوية اليمنى)
5. املأ النموذج:
   - University ID: CS2021010
   - Name: Your Name
   - Email: yourname@test.com
6. اضغط "Save"
7. سترى رمز QR تم توليده تلقائياً!
```

---

### تجربة 2: عرض إحصائيات الطالب

```
1. اذهب إلى: http://localhost:8000/students/
2. ابحث عن الطالب الذي أضفته
3. اضغط على "View" بجانب اسمه
4. سترى:
   - معلومات الطالب الكاملة
   - رمز QR الخاص به
   - نسبة الحضور
   - سجل الحضور التفصيلي
   - الشارات المكتسبة (إن وجدت)
```

---

### تجربة 3: تسجيل حضور

```
1. اذهب إلى: http://localhost:8000/scanner/
2. اختر جلسة من القائمة (مثلاً: Database Design)
3. اختر حالة: "Present"
4. في حقل "Enter Student UUID Manually"، أدخل:
   STUDENT: ثم UUID الطالب (يمكن نسخه من صفحة الطالب)
5. اضغط "Submit"
6. سترى رسالة نجاح وسيظهر اسم الطالب
```

---

### تجربة 4: عرض التقارير

```
1. اذهب إلى: http://localhost:8000/dashboard/
2. شاهد الإحصائيات المحدّثة
3. اضغط "Export to Excel"
4. سيتم تحميل ملف Excel يحتوي على:
   - قائمة الطلاب
   - نسب الحضور
   - عدد الحضور والغياب لكل طالب
```

---

## 📊 البيانات النموذجية | Sample Data

النظام محمّل بالفعل ببيانات نموذجية:
The system is already loaded with sample data:

### الطلاب | Students (5)
1. **Ahmad Hassan** (CS2021001) - 75% حضور
2. **Fatima Ali** (CS2021002) - 75% حضور
3. **Mohammed Khalil** (CS2021003) - 100% حضور
4. **Sara Ibrahim** (CS2021004) - 75% حضور
5. **Omar Nasser** (CS2021005) - 100% حضور

### الجلسات | Sessions (5)
1. Introduction to Programming (محاضرة)
2. Data Structures Lab (معمل)
3. Algorithms Lecture (محاضرة)
4. Midterm Exam (امتحان)
5. Database Design (محاضرة)

يمكنك استعراض هذه البيانات والتعديل عليها!
You can browse and modify this data!

---

## 🔧 نصائح وحلول | Tips & Solutions

### مشكلة: الصفحة لا تفتح
**الحل:**
1. تأكد أن الخادم يعمل (Terminal مفتوح ويظهر "Starting server")
2. تأكد من الرابط الصحيح: http://127.0.0.1:8000/
3. جرب http://localhost:8000/ بدلاً منه
4. أعد تشغيل الخادم:
   ```bash
   Ctrl+C لإيقافه
   python3 manage.py runserver لإعادة تشغيله
   ```

---

### مشكلة: نسيت كلمة المرور
**الحل:**
```bash
cd /home/runner/work/InfoSecNazir/InfoSecNazir
python3 manage.py changepassword admin
```

---

### مشكلة: الكاميرا لا تعمل في الماسح
**الحل:**
- استخدم الإدخال اليدوي بدلاً منها
- أو استخدم HTTPS (الكاميرا تتطلب HTTPS في بعض المتصفحات)
- أو استخدم متصفح آخر

---

## 🎓 سيناريوهات الاستخدام | Use Cases

### سيناريو 1: تسجيل حضور محاضرة
```
1. المدرس يفتح صفحة الماسح
2. يختار "محاضرة قواعد البيانات"
3. يختار "Present"
4. الطلاب يعرضون رموز QR
5. المدرس يمسح كل رمز
6. النظام يسجل الحضور تلقائياً
7. المدرس يمكنه رؤية قائمة الحاضرين فوراً
```

---

### سيناريو 2: تتبع طالب معرض للخطر
```
1. المدرس يفتح Dashboard
2. يرى قسم "At Risk Students"
3. يجد طلاب حضورهم أقل من 50%
4. ينقر على الطالب لرؤية التفاصيل
5. يرى سجل الحضور الكامل
6. يمكن اتخاذ إجراء (تنبيه، استشارة، إلخ)
```

---

### سيناريو 3: إنشاء تقرير للإدارة
```
1. في نهاية الشهر/الفصل
2. المدرس يفتح Dashboard
3. يضغط "Export to Excel"
4. يحصل على ملف Excel احترافي
5. يرفعه للإدارة مباشرة
6. التقرير يحتوي على جميع البيانات منسقة
```

---

## 📱 الوصول من الهاتف | Mobile Access

يمكنك الوصول من الهاتف أيضاً!
You can access from mobile too!

**إذا كنت على نفس الشبكة:**
1. احصل على IP address للكمبيوتر
   ```bash
   ipconfig  # في Windows
   ifconfig  # في Mac/Linux
   ```
2. من الهاتف، افتح المتصفح واكتب:
   ```
   http://[IP_ADDRESS]:8000/
   ```

**مثال:**
```
http://192.168.1.100:8000/
```

الواجهة responsive وتعمل بشكل ممتاز على الهواتف!
The interface is responsive and works great on phones!

---

## 🎯 ملخص سريع | Quick Summary

**للبدء السريع:**
```bash
# 1. تشغيل النظام
python3 manage.py runserver

# 2. فتح المتصفح
http://localhost:8000/

# 3. تسجيل الدخول
admin / admin123

# 4. ابدأ التجربة!
```

**الصفحات الرئيسية:**
- 🏠 الرئيسية: http://localhost:8000/
- 📊 Dashboard: http://localhost:8000/dashboard/
- 👨‍🎓 الطلاب: http://localhost:8000/students/
- 📅 الجلسات: http://localhost:8000/sessions/
- 📷 الماسح: http://localhost:8000/scanner/
- ⚙️ الإدارة: http://localhost:8000/admin/

---

## 🆘 هل تحتاج مساعدة؟ | Need Help?

- **البريد:** Hnzyr31@gmail.com
- **GitHub:** [@InfoSecNazir](https://github.com/InfoSecNazir)
- **الملفات:** راجع DEPLOYMENT_READY.md للتفاصيل الكاملة

---

## ✅ جاهز للتجربة! | Ready to Try!

الآن أنت جاهز لتجربة النظام! ابدأ بالخطوة 1️⃣ واستمتع بالتجربة.

Now you're ready to try the system! Start with Step 1️⃣ and enjoy!

**🎉 استمتع باستخدام نظام إدارة الطلاب الذكي! 🎉**
**🎉 Enjoy using the Smart Student Management System! 🎉**

---

**آخر تحديث:** 13 فبراير 2026  
**Last Updated:** February 13, 2026
