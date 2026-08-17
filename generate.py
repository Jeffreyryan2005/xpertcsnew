import os

header_html = '''    <!-- Header -->
    <header class="site-header site-header--transparent">
        <div class="site-header__inner">
            <a href="index.html" class="logo" aria-label="Xpert Consultancy Home">
                <img src="https://www.xpertcs.com/assets/img/logo.png" alt="Xpert Consultancy Logo" class="logo-img">
            </a>

            <button class="nav-toggle" aria-label="Toggle navigation">
                <span></span>
                <span></span>
                <span></span>
            </button>

            <nav class="nav">
                <ul class="nav__list">
                    <li class="nav__item">
                        <a href="index.html" class="nav__link">Home</a>
                    </li>
                    <li class="nav__item">
                        <a href="about.html" class="nav__link">About Us</a>
                        <div class="nav__dropdown">
                            <a href="about.html#who-we-are" class="nav__dropdown-link">Who We Are</a>
                            <a href="about.html#what-we-do" class="nav__dropdown-link">What We Do</a>
                            <a href="about.html#how-we-do" class="nav__dropdown-link">How We Do It</a>
                            <a href="about.html#why-xpert" class="nav__dropdown-link">Why Xpert Consultancy</a>
                        </div>
                    </li>
                    <li class="nav__item">
                        <a href="services.html" class="nav__link">Services</a>
                        <div class="nav__dropdown">
                            <a href="cloud-technologies.html" class="nav__dropdown-link">Cloud Technologies</a>
                            <a href="secure-infrastructure.html" class="nav__dropdown-link">Secure Infrastructure</a>
                            <a href="it-consultancy.html" class="nav__dropdown-link">IT Consultancy</a>
                            <a href="managed-services.html" class="nav__dropdown-link">Managed Services</a>
                        </div>
                    </li>
                    <li class="nav__item"><a href="knowledge-base.html" class="nav__link">Knowledge Base</a></li>
                    <li class="nav__item"><a href="partners.html" class="nav__link">Partners</a></li>
                    <li class="nav__item"><a href="contact.html" class="nav__link">Contact Us</a></li>
                    <li class="nav__item">
                        <a href="https://helpdesk.xpertcs.com/login?redirectTo=%2F" target="_blank" rel="noopener noreferrer" class="nav__cta">Help Desk</a>
                    </li>
                </ul>
            </nav>
        </div>
    </header>'''

footer_html = '''    <!-- Footer -->
    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <!-- About -->
                <div class="footer-widget reveal">
                    <h3 class="footer__heading">About Us</h3>
                    <p class="footer__text">We are a fast-growing business providing IT consultancy and technology solutions. With a reputation for understanding industry-specific requirements, we respond with quality service and support.</p>
                </div>

                <!-- Services -->
                <div class="footer-widget reveal reveal-delay-1">
                    <h3 class="footer__heading">Our Services</h3>
                    <nav class="footer__links">
                        <a href="cloud-technologies.html" class="footer__link">Cloud Technologies</a>
                        <a href="secure-infrastructure.html" class="footer__link">Secure Infrastructure</a>
                        <a href="it-consultancy.html" class="footer__link">IT Consultancy</a>
                        <a href="managed-services.html" class="footer__link">Managed Services</a>
                    </nav>
                </div>

                <!-- Quick Links -->
                <div class="footer-widget reveal reveal-delay-2">
                    <h3 class="footer__heading">Quick Links</h3>
                    <nav class="footer__links">
                        <a href="index.html" class="footer__link">Home</a>
                        <a href="about.html" class="footer__link">About Us</a>
                        <a href="knowledge-base.html" class="footer__link">Knowledge Base</a>
                        <a href="partners.html" class="footer__link">Partners</a>
                        <a href="https://helpdesk.xpertcs.com/login?redirectTo=%2F" target="_blank" rel="noopener noreferrer" class="footer__link">Help Desk</a>
                    </nav>
                </div>

                <!-- Contact -->
                <div class="footer-widget reveal reveal-delay-3">
                    <h3 class="footer__heading">Contact Info</h3>
                    <address class="footer__contact-list">
                        <div class="footer__contact-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            <div>
                                <strong>Xpert Consultancy Ltd</strong>
                                71-75 Shelton Street<br>London, England<br>WC2H 9JQ
                            </div>
                        </div>
                        <div class="footer__contact-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
                            <a href="mailto:enquiry@xpertcs.com">enquiry@xpertcs.com</a>
                        </div>
                        <div class="footer__contact-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                            <a href="tel:02073607595">0207 360 7595</a>
                        </div>
                    </address>
                </div>
            </div>

            <div class="footer__bottom">
                <div class="footer__copyright">
                    &copy; 2026 Xpert Consultancy Limited. All Rights Reserved.
                </div>
                <div class="footer__bottom-links">
                    <a href="terms-and-conditions.html">Terms & Conditions</a>
                    <a href="legal-disclaimer.html">Legal Disclaimer</a>
                    <a href="privacy-policy.html">Privacy Policy</a>
                </div>
            </div>
        </div>
    </footer>'''

def get_base_html(title, content):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Xpert Consultancy</title>
    <meta name="description" content="Xpert Consultancy provides expert IT consultancy, cloud technologies, secure infrastructure, and managed services for enterprises.">
    
    <!-- Favicon -->
    <link rel="shortcut icon" type="image/x-icon" href="https://www.xpertcs.com/assets/img/favicon.png">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <!-- CSS -->
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
{header_html}

{content}

{footer_html}

    <!-- Scripts -->
    <script src="js/main.js"></script>
</body>
</html>'''

pages = {
    'about.html': {
        'title': 'About Us',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">About Us</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <span class="current">About Us</span>
            </div>
        </div>
    </section>

    <section id="who-we-are" class="section section--cream">
        <div class="container">
            <div class="content-split">
                <div class="content-block__text">
                    <p class="content-block__label label-text">Who We Are</p>
                    <h2 class="heading-accent content-block__title">No-nonsense advice and practical solutions.</h2>
                    <p>We are a fast-growing business who understand the pressures you operate under. Our company has a reputation for understanding the industry-specific requirements of each client and responding to them with quality service and support. With over 20 years of experience, we align technology with your business outcomes.</p>
                </div>
                <div class="content-block__image">
                    <img src="https://www.xpertcs.com/assets/img/about-us.png" alt="Who We Are">
                </div>
            </div>
        </div>
    </section>'''
    },
    'cloud-technologies.html': {
        'title': 'Cloud Technologies',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">Cloud Technologies</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <a href="services.html">Services</a>
                <span>/</span>
                <span class="current">Cloud Technologies</span>
            </div>
        </div>
    </section>

    <section class="section section--cream">
        <div class="container">
            <div class="content-split">
                <div class="content-block__text">
                    <h2 class="heading-accent content-block__title">Navigate Your Cloud Journey Confidently</h2>
                    <p>We plan, design, and implement scalable architectures on Azure, AWS, and Microsoft 365. Whether you are migrating legacy systems to the cloud, building cloud-native applications, or optimizing your existing cloud spend, Xpert Consultancy has the expertise to guide you.</p>
                </div>
                <div class="content-block__image">
                    <img src="https://www.xpertcs.com/assets/img/slider-1.jpg" alt="Cloud Technologies">
                </div>
            </div>
        </div>
    </section>'''
    },
    'secure-infrastructure.html': {
        'title': 'Secure Infrastructure',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">Secure Infrastructure</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <a href="services.html">Services</a>
                <span>/</span>
                <span class="current">Secure Infrastructure</span>
            </div>
        </div>
    </section>

    <section class="section section--warm">
        <div class="container">
            <div class="content-split content-split--reverse">
                <div class="content-block__text">
                    <h2 class="heading-accent content-block__title">Protect Your Business in the Public Cloud</h2>
                    <p>Security is paramount in today’s landscape. We specialize in remote work security, identity protection, and disaster recovery. From robust firewall configurations to zero-trust architecture, our secure infrastructure solutions ensure your enterprise data remains safe and compliant at all times.</p>
                </div>
                <div class="content-block__image">
                    <img src="https://www.xpertcs.com/assets/img/slider-1.jpg" alt="Secure Infrastructure">
                </div>
            </div>
        </div>
    </section>'''
    },
    'it-consultancy.html': {
        'title': 'IT Consultancy',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">IT Consultancy</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <a href="services.html">Services</a>
                <span>/</span>
                <span class="current">IT Consultancy</span>
            </div>
        </div>
    </section>

    <section class="section section--cream">
        <div class="container">
            <div class="content-split">
                <div class="content-block__text">
                    <h2 class="heading-accent content-block__title">Expert Guidance for Enterprise IT</h2>
                    <p>Expert guidance for change management, mergers, and technology investments. We align your IT strategy with business goals. Let our experienced consultants help you navigate complex technological landscapes and unlock the full potential of your IT investments.</p>
                </div>
                <div class="content-block__image">
                    <img src="https://www.xpertcs.com/assets/img/about-us.png" alt="IT Consultancy">
                </div>
            </div>
        </div>
    </section>'''
    },
    'managed-services.html': {
        'title': 'Managed Services',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">Managed Services</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <a href="services.html">Services</a>
                <span>/</span>
                <span class="current">Managed Services</span>
            </div>
        </div>
    </section>

    <section class="section section--warm">
        <div class="container">
            <div class="content-split content-split--reverse">
                <div class="content-block__text">
                    <h2 class="heading-accent content-block__title">An Extension of Your ICT Department</h2>
                    <p>We offer 24/7/365 support for servers, networks, applications, and end-users. Offload your day-to-day IT operations to Xpert Consultancy and focus on what you do best: growing your business. Our managed services provide peace of mind and predictable IT costs.</p>
                </div>
                <div class="content-block__image">
                    <img src="https://www.xpertcs.com/assets/img/slider-1.jpg" alt="Managed Services">
                </div>
            </div>
        </div>
    </section>'''
    },
    'services.html': {
        'title': 'Our Services',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">Our Services</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <span class="current">Services</span>
            </div>
        </div>
    </section>

    <section class="section section--cream">
        <div class="container">
            <div class="services-grid">
                <a href="cloud-technologies.html" class="service-card reveal reveal-delay-1">
                    <div class="service-card__icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"></path></svg>
                    </div>
                    <h3 class="service-card__title">Cloud Technologies</h3>
                    <p class="service-card__text">Navigate your cloud journey confidently. We plan, design, and implement scalable architectures on Azure, AWS, and Microsoft 365.</p>
                    <span class="link-arrow">Learn more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg></span>
                </a>
                
                <a href="secure-infrastructure.html" class="service-card reveal reveal-delay-2">
                    <div class="service-card__icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                    </div>
                    <h3 class="service-card__title">Secure Infrastructure</h3>
                    <p class="service-card__text">Protect your business in the public cloud. We specialize in remote work security, identity protection, and disaster recovery.</p>
                    <span class="link-arrow">Learn more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg></span>
                </a>

                <a href="it-consultancy.html" class="service-card reveal reveal-delay-3">
                    <div class="service-card__icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
                    </div>
                    <h3 class="service-card__title">IT Consultancy</h3>
                    <p class="service-card__text">Expert guidance for change management, mergers, and technology investments. We align your IT strategy with business goals.</p>
                    <span class="link-arrow">Learn more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg></span>
                </a>

                <a href="managed-services.html" class="service-card reveal reveal-delay-4">
                    <div class="service-card__icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"></path><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                    </div>
                    <h3 class="service-card__title">Managed Services</h3>
                    <p class="service-card__text">An extension of your ICT department. We offer 24/7/365 support for servers, networks, applications, and end-users.</p>
                    <span class="link-arrow">Learn more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg></span>
                </a>
            </div>
        </div>
    </section>'''
    },
    'partners.html': {
        'title': 'Partners',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">Our Partners</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <span class="current">Partners</span>
            </div>
        </div>
    </section>

    <section class="section section--cream">
        <div class="container">
            <div class="partners-grid">
                <div class="partner-logo-card">
                    <img src="https://www.xpertcs.com/assets/img/partner-img1.png" alt="Partner">
                </div>
                <div class="partner-logo-card">
                    <img src="https://www.xpertcs.com/assets/img/partner-img2.png" alt="Partner">
                </div>
                <div class="partner-logo-card">
                    <img src="https://www.xpertcs.com/assets/img/partner-img3.png" alt="Partner">
                </div>
                <div class="partner-logo-card">
                    <img src="https://www.xpertcs.com/assets/img/partner-img4.png" alt="Partner">
                </div>
                <div class="partner-logo-card">
                    <img src="https://www.xpertcs.com/assets/img/partner-img5.png" alt="Partner">
                </div>
                <div class="partner-logo-card">
                    <img src="https://www.xpertcs.com/assets/img/partner-img6.jpg" alt="Partner">
                </div>
                <div class="partner-logo-card">
                    <img src="https://www.xpertcs.com/assets/img/partner-img7.jpg" alt="Partner">
                </div>
                <div class="partner-logo-card">
                    <img src="https://www.xpertcs.com/assets/img/partner-img8.jpg" alt="Partner">
                </div>
            </div>
        </div>
    </section>'''
    },
    'knowledge-base.html': {
        'title': 'Knowledge Base',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">Knowledge Base</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <span class="current">Knowledge Base</span>
            </div>
        </div>
    </section>

    <section class="section section--cream">
        <div class="container container--narrow text-center">
            <h2 class="heading-accent" style="margin-bottom:1rem;">Coming Soon</h2>
            <p>Our knowledge base is currently being updated. Please check back later for comprehensive IT guides, FAQs, and resources.</p>
        </div>
    </section>'''
    },
    'contact.html': {
        'title': 'Contact Us',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">Contact Us</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <span class="current">Contact Us</span>
            </div>
        </div>
    </section>

    <section class="section section--cream">
        <div class="container">
            <div class="contact-grid">
                <div class="contact-info">
                    <h2 class="heading-accent" style="margin-bottom: 2rem;">Get in Touch</h2>
                    <div class="contact-info__item">
                        <div class="contact-info__icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                        </div>
                        <div>
                            <p class="contact-info__label">Head Office</p>
                            <p class="contact-info__value">71-75 Shelton Street, London, England, WC2H 9JQ</p>
                        </div>
                    </div>
                    <div class="contact-info__item">
                        <div class="contact-info__icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                        </div>
                        <div>
                            <p class="contact-info__label">Phone</p>
                            <p class="contact-info__value"><a href="tel:02073607595">0207 360 7595</a></p>
                        </div>
                    </div>
                    <div class="contact-info__item">
                        <div class="contact-info__icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
                        </div>
                        <div>
                            <p class="contact-info__label">Email</p>
                            <p class="contact-info__value"><a href="mailto:enquiry@xpertcs.com">enquiry@xpertcs.com</a></p>
                        </div>
                    </div>
                </div>

                <div class="contact-form">
                    <form action="mailto:enquiry@xpertcs.com" method="post" enctype="text/plain">
                        <div style="margin-bottom: 1rem;">
                            <label for="name" style="display: block; margin-bottom: 0.5rem; font-size: var(--fs-small); color: var(--clr-charcoal); font-weight: 500;">Name:</label>
                            <input type="text" id="name" name="name" required style="width: 100%; padding: 0.8rem; border: 1px solid var(--clr-light-grey); border-radius: 4px; font-family: var(--ff-body);">
                        </div>
                        <div style="margin-bottom: 1rem;">
                            <label for="email" style="display: block; margin-bottom: 0.5rem; font-size: var(--fs-small); color: var(--clr-charcoal); font-weight: 500;">Email:</label>
                            <input type="email" id="email" name="email" required style="width: 100%; padding: 0.8rem; border: 1px solid var(--clr-light-grey); border-radius: 4px; font-family: var(--ff-body);">
                        </div>
                        <div style="margin-bottom: 1rem;">
                            <label for="message" style="display: block; margin-bottom: 0.5rem; font-size: var(--fs-small); color: var(--clr-charcoal); font-weight: 500;">Message:</label>
                            <textarea id="message" name="message" rows="5" required style="width: 100%; padding: 0.8rem; border: 1px solid var(--clr-light-grey); border-radius: 4px; font-family: var(--ff-body);"></textarea>
                        </div>
                        <button type="submit" class="btn btn--primary" style="width: 100%; justify-content: center;">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>'''
    },
    'terms-and-conditions.html': {
        'title': 'Terms & Conditions',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">Terms & Conditions</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <span class="current">Terms & Conditions</span>
            </div>
        </div>
    </section>

    <section class="section section--cream">
        <div class="container container--narrow">
            <div class="content-block__text">
                <h2 class="heading-accent">Terms of Use</h2>
                <p>Welcome to Xpert Consultancy. By using our website and services, you agree to comply with and be bound by the following terms and conditions of use. If you disagree with any part of these terms and conditions, please do not use our website.</p>
                <p>We reserve the right to modify these terms at any time without prior notice. Changes will be posted on this page.</p>
            </div>
        </div>
    </section>'''
    },
    'legal-disclaimer.html': {
        'title': 'Legal Disclaimer',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">Legal Disclaimer</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <span class="current">Legal Disclaimer</span>
            </div>
        </div>
    </section>

    <section class="section section--cream">
        <div class="container container--narrow">
            <div class="content-block__text">
                <h2 class="heading-accent">Disclaimer of Liability</h2>
                <p>The information contained in this website is for general information purposes only. The information is provided by Xpert Consultancy and while we endeavour to keep the information up to date and correct, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability with respect to the website or the information, products, services, or related graphics contained on the website for any purpose.</p>
            </div>
        </div>
    </section>'''
    },
    'privacy-policy.html': {
        'title': 'Privacy Policy',
        'content': '''    <section class="page-header">
        <div class="container page-header__content">
            <h1 class="page-header__title">Privacy Policy</h1>
            <div class="page-header__breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <span class="current">Privacy Policy</span>
            </div>
        </div>
    </section>

    <section class="section section--cream">
        <div class="container container--narrow">
            <div class="content-block__text">
                <h2 class="heading-accent">Your Privacy Matters</h2>
                <p>At Xpert Consultancy, we are committed to protecting your privacy and ensuring the security of your personal information. This Privacy Policy outlines how we collect, use, disclose, and safeguard your data when you visit our website or use our services.</p>
                <p>We may collect personal identification information from Users in a variety of ways, including, but not limited to, when Users visit our site, fill out a form, and in connection with other activities, services, features or resources we make available on our Site.</p>
            </div>
        </div>
    </section>'''
    }
}

for filename, data in pages.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(get_base_html(data['title'], data['content']))
