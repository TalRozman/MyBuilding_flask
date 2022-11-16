from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return '''
<!DOCTYPE html>
<html lang="he" style="direction: rtl;">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>בני משה 18</title>
  <link rel="shortcut icon" href="static/img/home.png" type="image/x-icon">
  <meta content="" name="description">
  <meta content="" name="keywords">
  <!-- Favicons -->
  <link href="static/img/favicon.png" rel="icon">
  <link href="static/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="static/vendor/aos/aos.css" rel="stylesheet">
  <link href="static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="static/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="static/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
  <link href="static/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="static/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="static\css\style.css" rel="stylesheet">
</head>

<body>
  <!-- ======= Header ======= -->
  <header id="header" class="d-flex align-items-center">
    <div class="container d-flex align-items-center justify-content-between">

      <h1 class="logo"><a href="/">בני משה 18</a></h1>

      <nav id="navbar" class="navbar">
        <ul>
          <li><a class="nav-link scrollto active" href="#welcome">בית</a></li>
          <li><a class="nav-link scrollto" href="#lobi">לוח מודעות</a></li>
          <li><a class="nav-link scrollto" href="#pricing">תשלומי ועד בית</a></li>
          <li><a class="nav-link scrollto" href="#team">הנפשות הפועלות</a></li>
          <li><a class="nav-link scrollto" href="#contact">מידע נוסף</a></li>
        </ul>
        <i class="bi bi-list mobile-nav-toggle"></i>
      </nav><!-- .navbar -->
    </div>
  </header><!-- End Header -->

  <!-- ======= Welcome Section ======= -->
  <section id="welcome" class="d-flex align-items-center">
    <div class="container position-relative" data-aos="fade-up" data-aos-delay="500">
      <h1>בני משה 18 רחובות</h1>
      <!-- <h2>למען שכנות טובה</h2> -->
    </div>
  </section><!-- End Welcome -->

  <main id="main">

    <!-- ======= lobi Section ======= -->
    <section id="lobi" class="lobi">
      <div class="container">

        <div class="row">
          <div class="col-lg-6 order-1 order-lg-2" data-aos="fade-left">
            <img src="static/img/lobi.jpeg" class="img-fluid" alt="" width="85%">
          </div>

          <div class="col-lg-6 pt-4 pt-lg-0 order-2 order-lg-1 content" data-aos="fade-right">
            <div id="scroll-container" style="font-size: 40px;">
              <div id="scroll-text">
                שעות מעלית שבת<br>
                שישי - 19:00 - 18:30<br>
                שבת - 10:45 - 10:15<br>
                ********<br>
                שלום רב<br>
                ב-26 לחודש תתקיים אסיפת דיירים <br>
                בלובי הבניין בשעה 20:00<br>
                ההשתתפות הינה חובה<br>
                תודה<br>
                ********<br>
              </div>
            </div>
          </div>

        </div>
    </section>
    <!-- End About Section -->

    <!-- ======= drone_pic Section ======= -->
    <section id="drone_pic" class="drone_pic">
      <div class="container" data-aos="zoom-in">
        <div class="text-center">
          <br><br><br><br><br><br><br>
        </div>
      </div>
    </section>
    <!-- End drone_pic Section -->

    <!-- ======= Pricing Section ======= -->
    <section id="pricing" class="pricing">
      <div class="container">

        <div class="section-title">
          <span>תשלומי ועד בית</span>
          <h2>תשלומי ועד בית</h2>
          <p>על פי החלטת הדיירים באסיפת דיירים האחרונה, להלן דמי ועד בית לשנת 2023:</p>
        </div>

        <div class="row">

          <div class="col-lg-4 col-md-6" data-aos="zoom-in" data-aos-delay="150">
            <div class="box">
              <h3>דירת ארבעה חדרים</h3>
              <h4><sup>₪</sup>200<span> לחודש</span></h4>
              <div class="btn-wrap">
                <a href="#payments" class="btn-buy" onclick="send_payment(200);ShowAndHide()">שלם עכשיו!</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 mt-4 mt-md-0" data-aos="zoom-in">
            <div class="box">
              <h3>דירת חמישה חדרים</h3>
              <h4><sup>₪</sup>250<span> לחודש</span></h4>
              <div class="btn-wrap">
                <a href="#payments" class="btn-buy" onclick="send_payment(250);ShowAndHide()">שלם עכשיו!</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 mt-4 mt-lg-0" data-aos="zoom-in" data-aos-delay="150">
            <div class="box">
              <h3>דירת פנטאוז/גן</h3>
              <h4><sup>₪</sup>300<span> לחודש</span></h4>
              <div class="btn-wrap">  
                <a href="#payments" class="btn-buy" onclick="send_payment(300);ShowAndHide()">שלם עכשיו!</a>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>
    <!-- End Pricing Section -->

    <!-- ======= Services Section ======= -->
    <section id="payments" class="services" style="display: none;">
      <div class="container">
        <div class="section-title">
          <span>דף תשלום לועד הבית</span>
          <h2>דף תשלום לועד הבית</h2>
        </div>
        <div class="container">
          <main>   
            <div class="row g-5" style="text-align: right">
              <div class="col-md-5 col-lg-4 order-md-last">
                <h4 class="d-flex justify-content-between align-items-center mb-3">
                  <span class="text-primary">הסל שלי</span>
                  <span class="badge bg-primary rounded-pill">1</span>
                </h4>
                <ul class="list-group mb-3">
                  <li class="list-group-item d-flex justify-content-between lh-sm">
                    <div>
                      <h6 class="my-0">תשלום ועד בית חודשי</h6>
                    </div>
                    <span class="text-muted" id="product_price"></span>
                  </li>
                  </li>
                  <li class="list-group-item d-flex justify-content-between">
                    <span>סה"כ לתשלום</span>
                    <span id="product_price1"></span>
                  </li>
                </ul>
              </div>
              <div class="col-md-7 col-lg-8">
                <h4 class="mb-3">פרטי המשלם</h4>
                <form class="needs-validation" novalidate>
                  <div class="row g-3">
                    <div class="col-sm-6">
                      <label for="firstName" class="form-label">שם פרטי</label>
                      <input type="text" class="form-control" id="firstName" placeholder="" value="" required>
                      <div class="invalid-feedback">
                        נא להזין שם פרטי
                      </div>
                    </div>
      
                    <div class="col-sm-6">
                      <label for="lastName" class="form-label">שם משפחה</label>
                      <input type="text" class="form-control" id="lastName" placeholder="" value="" required>
                      <div class="invalid-feedback">
                        נא להזין שם משפחה
                      </div>
                    </div>

                    <div class="col-12">
                      <label for="email" class="form-label">כתובת דוא"ל <span class="text-muted">אופציונלי</span></label>
                      <input type="email" class="form-control" id="email" placeholder="you@example.com">
                      <div class="invalid-feedback">
                        נא להזין כתובת דוא"ל תקינה
                      </div>
                    </div>
      
                    <div class="col-12">
                      <label for="address" class="form-label">כתובת מגורים</label>
                      <input type="text" class="form-control" id="address" placeholder="" required>
                      <div class="invalid-feedback">
                        נא להזין כתובת מגורים
                      </div>
                    </div>
      
                    <div class="col-md-4">
                      <label for="city" class="form-label">עיר</label>
                      <select class="form-select" id="city" required>
                        <option value="">בחר</option>
                        <option>תל אביב</option>
                        <option>רחובות</option>
                        <option>נתניה</option>
                        <option>ראשון לציון</option>
                        <option>אשדוד</option>
                        <option>יבנה</option>
                        <option>מודיעין</option>
                      </select>
                      <div class="invalid-feedback">
                        נא להזין עיר מגורים
                      </div>
                    </div>        

                  <hr class="my-4">
      
                  <h4 class="mb-3">תשלום</h4>
      
                  <div class="my-3">
                    <div class="form-check">
                      <label class="form-check-label" for="credit">כרטיס אשראי</label>
                      <input id="credit" name="paymentMethod" type="radio" value="CC" class="form-check-input" required checked onclick="payment_method()">
                    </div>
                    <div class="form-check">
                      <label class="form-check-label" for="bank">העברה בנקאית</label>
                      <input id="bank" name="paymentMethod" type="radio" value="bank" class="form-check-input" required onclick="payment_method()">
                    </div>

                    <div class="form-check">
                      <label class="form-check-label" for="paypal">PayPal</label>
                      <input id="paypal" name="paymentMethod" type="radio" value="paypal" class="form-check-input" required onclick="payment_method()">
                    </div>
                  </div>
                  <div id="credit_form">
                    <div class="row gy-3">
                      <div class="col-md-6">
                        <label for="cc-name" class="form-label">שם בעל הכרטיס</label>
                        <input type="text" class="form-control" id="cc-name" placeholder="" required>
                        <small class="text-muted">שם מלא ככתוב על הכרטיס</small>
                        <div class="invalid-feedback">
                          נא להזין שם בעל הכרטיס
                        </div>
                      </div>
        
                      <div class="col-md-6" >
                        <label for="cc-number" class="form-label">מספר כרטיס אשראי</label>
                        <input type="text" class="form-control" id="cc-number" placeholder="" required>
                        <div class="invalid-feedback">
                          נא להזין מספר כרטיס אשראי תקין
                        </div>
                      </div>
        
                      <div class="col-md-3">
                        <label for="cc-expiration" class="form-label">תוקף הכרטיס</label>
                        <input type="month" class="form-control" id="cc-expiration" placeholder="" required>
                        <div class="invalid-feedback">
                          נא להזין תוקף תקין
                        </div>
                      </div>
        
                      <div class="col-md-3">
                        <label for="cc-cvv" class="form-label">CVV</label>
                        <input type="text" class="form-control" id="cc-cvv" placeholder="" required>
                        <small class="text-muted">שלושת הספרות על גב הכרטיס</small>
                        <div class="invalid-feedback">
                          נא להזין CVV תקין
                        </div>
                      </div>
                    </div>
                    <hr class="my-4">
                    <button class="w-100 btn btn-primary btn-lg" type="submit">בצע תשלום באמצעות כרטיס אשראי</button>
                  </div>

                  <div id="bank_form" style="display: none;">
                      <div class="col-lg-6">
                        <div class="info-box mb-4">
                          <h3>פרטי חשבון בנק להעברת כספים:</h3><br>
                          <p>בנק: 8<br>סניף: 333<br>מספר חשבון: 234512</p>
                        </div>
                      </div>
                  </div>

                  <div id="paypal_form" style="display: none;">
                    <hr class="my-4">
                    <button class="w-100 btn btn-primary btn-lg" type="submit">בצע תשלום באמצעות PAYPAL</button>
                  </div>
                </form>
              </div>
            </div>
          </main>
        </div>
      </div>
    </section>
    <!-- End Services Section -->

    <!-- ======= night Section ======= -->
    <section id="night" class="night">
      <div class="container" data-aos="zoom-in">
        <div class="text-center">
          <br><br><br><br><br><br><br>
        </div>
      </div>
    </section><!-- End Cta Section -->

    <!-- ======= Team Section ======= -->
    <section id="team" class="team">
      <div class="container">

        <div class="section-title">
          <span>צוות ועד הבית</span>
          <h2>צוות ועד הבית</h2>
        </div>

        <div class="row">
          <div class="col-lg-4 col-md-6 d-flex align-items-stretch" data-aos="zoom-in">
            <div class="member">
              <img src="static/img/team/team-1.jpg" alt="">
              <h4>ערן</h4>
              <span>יו"ר ועד הבית</span>
              <p>
                דירה מספר 16<br>
                מספר טלפון: 054362784285
              </p>
              <div class="social">
                <i class="bi bi-twitter"></i>
                <i class="bi bi-facebook"></i>
                <i class="bi bi-instagram"></i>
                <i class="bi bi-linkedin"></i>
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch" data-aos="zoom-in">
            <div class="member">
              <img src="static/img/team/team-2.jpg" alt="">
              <h4>אילנה</h4>
              <span>גזברית ועד הבית</span>
              <p>
                דירה מספר 5<br>
                מספר טלפון: 05347234756
              </p>
              <div class="social">
                <i class="bi bi-twitter"></i>
                <i class="bi bi-facebook"></i>
                <i class="bi bi-instagram"></i>
                <i class="bi bi-linkedin"></i>
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 d-flex align-items-stretch" data-aos="zoom-in">
            <div class="member">
              <img src="static/img/team/team-3.jpg" alt="">
              <h4>משה</h4>
              <span>חבר ועד הבית</span>
              <p>
                דירה מספר 8<br>
                מספר טלפון: 0527432646237
              </p>
              <div class="social">
                <i class="bi bi-twitter"></i>
                <i class="bi bi-facebook"></i>
                <i class="bi bi-instagram"></i>
                <i class="bi bi-linkedin"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- End Team Section -->

    <!-- ======= Contact Section ======= -->
    <section id="contact" class="contact">
      <div class="container">

        <div class="section-title">
          <span>מידע נוסף</span>
          <h2>מידע נוסף</h2>
          <p>לנוחיותכם, קישורים ליצירת קשר עם מוקד 106 העירוני, שליחת הודעה לוועד הבית וכתובת הבניין באנגלית</p>
        </div>

        <div class="row" data-aos="fade-up">
          <div class="col-lg-6">
            <div class="info-box mb-4">
              <i class="bx bx-map"></i>
              <h3>כתובת הבניין למשלוחים מאמזון ;)</h3><br>
              <p dir="ltr">18 Bnei Moshe st. Rehovot, Israel, 7648611</p>
            </div>
          </div>

          <div class="col-lg-3 col-md-6">
            <div class="info-box  mb-4">
              <i class="bx bx-phone-call"></i>
              <h3>פנייה למוקד עירוני</h3>
              <p dir="ltr"><a href="tel:083932106">:לפנייה באמצעות שיחת טלפון<br>08-393-2106</a></p>
            </div>
          </div>

          <div class="col-lg-3 col-md-6">
            <div class="info-box  mb-4">
              <i class="bx bx-phone-call"></i>
              <h3>פנייה למוקד עירוני</h3>
              <p><a href="https://api.whatsapp.com/send/?phone=972508806106&text&app_absent=0&lang=he">שליחת פנייה
                  באמצעות אפליקציית<br> Whatsapp</a></p>
            </div>
          </div>

        </div>

        <div class="row" data-aos="fade-up">

          <div class="col-lg-6 ">
            <iframe class="mb-4 mb-lg-0"
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3387.5307303380077!2d34.80879771460522!3d31.892174335880313!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1502b7198de9e729%3A0xbe791c27c134aea0!2sBnei%20Moshe%20St%2018%2C%20Rehovot!5e0!3m2!1sen!2sil!4v1668015274641!5m2!1sen!2sil"
              frameborder="0" style="border:0; width: 100%; height: 384px;" allowfullscreen></iframe>
          </div>

          <div class="col-lg-6">
            <form action="" method="" class="php-email-form">
              <div class="row">
                <div class="col-md-6 form-group">
                  <input type="text" name="name" class="form-control" id="name" placeholder="שם מלא" required>
                </div>
                <div class="col-md-6 form-group mt-3 mt-md-0">
                  <input type="tel" class="form-control" name="tel" id="tel" placeholder="מספר טלפון לחזרה" required>
                </div>
              </div>
              <div class="form-group mt-3">
                <input type="text" class="form-control" name="subject" id="subject" placeholder="נושא הפנייה" required>
              </div>
              <div class="form-group mt-3">
                <textarea class="form-control" name="message" rows="5" placeholder="תוכן הפנייה" required></textarea>
              </div>
              <div class="my-3">
                <div class="loading">טוען...</div>
                <div class="error-message"></div>
                <div class="sent-message">ההודעה נשלחה! נחזור אליך בהקדם</div>
              </div>
              <div class="text-center"><button type="submit">שלח</button></div>
            </form>
          </div>
        </div>
      </div>
    </section>
    <!-- End Contact Section -->

  </main>
  <!-- End #main -->

  <!-- ======= Footer ======= -->
  <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i
      class="bi bi-arrow-up-short"></i></a>
  <div id="preloader"></div>

  <!-- Vendor JS Files -->
  <script src="static/vendor/aos/aos.js"></script>
  <script src="static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="static/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="static/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="static/vendor/swiper/swiper-bundle.min.js"></script>
  <!-- Template Main JS File -->
  <script src="static/js/main.js"></script>
</body>

</html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
