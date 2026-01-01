# 📌 POST /api/signup/

Foydalanuvchi yangi account yaratadi va telefon raqamiga **OTP** yuboriladi.  
Ushbu endpoint orqali:

- Telefon raqami va **full name** bilan yangi user yaratish yoki mavjud userni olish
- Yangi OTP generatsiya qilinadi va **5 daqiqa** davomida amal qiladi

---

### 📝 Request Body
```json
    {
      "primary_mobile": "string",  
      "full_name": "string"         
    }
```

### ✅ Response Examples
### Success (200 OK) : 
```json:
    {
      "status": "success",
      "message": "Verification code sent to your mobile number.",
      "expiry": "5 minutes"
    }
```

### Warning (400 Bad Request) :
```json:
    {
      "status": "warning",
      "message": "Missing required fields."
    }
```

### Error (500 Internal Server Error)
```json:
    {
      "status": "error",
      "message": "An unexpected error occurred. Please try again later."
    }
```

- Har safar SignUp chaqirilganda eski OTP’lar o‘chiriladi
- OTP muddati: 5 daqiqa
### Response format: 
```json:
    {
      "status": "success | warning | error",
      "message": "string",
      "expiry": "string (success holatda)"
    }
```
---

---


# 📌 POST /api/otp-verify/
Foydalanuvchi telefon raqamini **verify** qilish uchun yuborilgan **OTP kodini** tekshiradi.

Ushbu endpoint orqali:  

- Telefon raqami va OTP to‘g‘ri bo‘lsa, foydalanuvchi `phone_verified = True` bo‘ladi  
- Agar OTP noto‘g‘ri bo‘lsa, muddati o‘tgan bo‘lsa yoki `attempts` ko‘p bo‘lsa, mos xabar qaytariladi  

---

---
### AllowAny (login qilmagan foydalanuvchi ham ishlata oladi), `request body`

```
{
  "primary_mobile": "string",   
  "otp_code": "string"          
}
```

### Response Examples `Success (200 OK)`
```{
  "status": "success",
  "message": "Mobile number verified successfully"
}
```

### Warning `(400 Bad Request)`
```
{
  "status": "warning",
  "message": "Missing required fields."
}
```


### Error (400 / 403)`OTP expired`
```{
  "status": "error",
  "message": "The verification code has expired. Please request a new one."
}
```

### Incorrect OTP
```
{
  "status": "error",
  "message": "The verification code is incorrect. You have 2 attempts left."
}
```


### Too many attempts (blocked)
```{
  "status": "error",
  "message": "Too many failed attempts. Try again later."
}
```


### User not found
```{
  "status": "error",
  "message": "No account was found with the provided information."
}
```
- OTP muddati: `5 daqiqa`
- Maksimal urinishlar: `5`
- Block vaqt: `10 daqiqa`

### Response format:
```{
  "status": "success | warning | error",
  "message": "string"
}
```

------

------


# POST /api/register-owner/ #
Assigns a user as Account Owner and updates user details. Only authorized users can call.

---
### Request Body: `Example:`
```json
{
  "primary_mobile": "+201234567890",
  "username": "Ahmed Ali",
  "email": "ahmed@example.com",
  "password": "StrongPass123"
}
```

### Responses, Success
```jsoN
{
  "status": "success",
  "message": "You have been assigned the role of Account Owner."
}
```


### Error – User not found
```json
{
  "status": "error",
  "message": "No account was found with the provided information."
}
```
HTTP Status: 400 Bad Request

### Error – Invalid invite link
```json
{
  "status": "error",
  "message": "The invitation link is invalid or has expired."
}
```
HTTP Status: 400 Bad Request


### Error – System error
```json
{
  "status": "error",
  "message": "An unexpected error occurred. Please try again later."
}
```
### HTTP Status: `500 Internal Server Error`


***Notes*** 
- `OTP` must be verified before assigning user as `Account Owner`
- Only users with proper permissions can call this endpoint
- All messages are standardized via `SUCCESS_MESSAGES and ERROR_MESSAGES`
---

---

