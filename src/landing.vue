<script setup>
import { onMounted } from "vue";
import { ref } from "vue";

const activeIndex = ref(null);
const targetElement = ref(null);
const targetElementFive = ref(null);
const targetAbout = ref(null);
const questionsTarget = ref(null);
const form = ref({
  procedureType: "",
  name: "",
  email: "",
  phone: "",
  dateRange: "",
  concerns: "",
});
const isSubmitting = ref(false);
const isSuccess = ref(false); // Tracks the "Sent !" state

const handleFormSubmit = async () => {
  isSubmitting.value = true;

  try {
    const response = await fetch("http://127.0.0.1:5000/api/schedule", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(form.value),
    });

    const result = await response.json();

    if (response.ok) {
      // 1. Clear the form fields immediately
      form.value = {
        procedureType: "",
        name: "",
        email: "",
        phone: "",
        dateRange: "",
        concerns: "",
      };

      // 2. Trigger the "Sent !" text state
      isSuccess.value = true;

      // 3. Wait 3 seconds, then flip the button text back
      setTimeout(() => {
        isSuccess.value = false;
      }, 3000);
    } else {
      alert(`Submission failed: ${result.error}`);
    }
  } catch (error) {
    console.error("Network Error:", error);
    alert("Could not connect to the backend server.");
  } finally {
    isSubmitting.value = false;
  }
};

const toggleItem = (index) => {
  if (activeIndex.value === index) {
    activeIndex.value = null; // Close if clicked again
  } else {
    activeIndex.value = index; // Open clicked item
  }
};

const scrollToSection = () => {
  targetElement.value?.scrollIntoView({ behavior: "smooth" });
};

const scrollToFive = () => {
  targetElementFive.value?.scrollIntoView({ behavior: "smooth" });
};

const aboutUsScroll = () => {
  targetAbout.value?.scrollIntoView({ behavior: "smooth" });
};

const questionsScroll = () => {
  questionsTarget.value?.scrollIntoView({ behavior: "smooth" });
};

// Data directly matching your video contents
const faqItems = ref([
  {
    tag: "Awareness",
    question: "Will I wake up during surgery?",
    answer:
      "Anesthesia awareness — being conscious during a procedure — is extremely rare, occurring in approximately 1 in 19,000 cases under general anesthesia. Your anesthesiologist uses continuous monitoring of your brain activity, vital signs, and anesthetic levels throughout the procedure. If you have a history of awareness or take certain medications, tell your anesthesiologist during your consultation — there are specific protocols that reduce risk further.",
  },
  {
    tag: "Pediatric",
    question: "Is anesthesia safe for my child?",
    answer:
      "Pediatric anesthesia is one of the most carefully studied areas in medicine. Children metabolize anesthetics differently than adults, which is why pediatric anesthesiologists complete specialized fellowship training. For routine procedures like tonsillectomies and ear tubes, the risk of serious complications is very low. We recommend asking specifically whether a pediatric anesthesiologist will be present for your child's procedure.",
  },
  {
    tag: "Elderly",
    question: "What are the risks of general anesthesia for someone over 70?",
    answer:
      "Age alone is not a contraindication for anesthesia, but it does change the calculation. Older patients are more sensitive to anesthetic agents, may have reduced organ reserve, and have a higher risk of post-operative cognitive dysfunction (POCD) — temporary confusion or memory changes after surgery. These risks are manageable with proper pre-operative assessment and tailored anesthetic technique. A thorough pre-anesthesia consultation is especially important for elderly patients.",
  },
  {
    tag: "Medications",
    question: "Which medications do I need to stop before surgery?",
    answer:
      "This varies by medication and procedure. Generally: blood thinners (warfarin, Eliquis, aspirin) are often paused 5–7 days before. Diabetes medications, especially metformin, may be held the day of surgery. Blood pressure medications are usually continued. Herbal supplements — especially garlic, ginkgo, St. John's Wort, and fish oil — should be stopped 1–2 weeks before. Never stop any medication without specific guidance from your anesthesiologist or surgeon.",
  },
  {
    tag: "Nausea",
    question: "Why do some people feel so sick after anesthesia?",
    answer:
      "Post-operative nausea and vomiting (PONV) affects roughly 30% of patients and up to 80% of high-risk patients. Risk factors include being female, history of motion sickness, non-smoking status, and use of opioid pain medications post-operatively. If you've experienced PONV before, tell your anesthesiologist — there are highly effective preventive medications that can be given during surgery, and modern anti-nausea protocols have dramatically reduced how common and severe this is.",
  },
  {
    tag: "Regional",
    question:
      "What's the difference between general, regional, and sedation anesthesia?",
    answer:
      "General anesthesia renders you completely unconscious and requires airway management. Regional anesthesia (epidurals, nerve blocks) numbs a specific area while you remain awake or lightly sedated — common for orthopedic procedures and childbirth. Monitored anesthesia care (MAC) or twilight sedation provides relaxation and pain control while you remain breathing on your own. The appropriate type depends on your procedure, health status, and preferences — your anesthesiologist will explain the options specific to your surgery.",
  },
]);

onMounted(() => {
  if ("scrollRestoration" in history) {
    history.scrollRestoration = "manual";
  }

  // 2. Use a micro-timeout to wait until the browser finishes layout processing
  setTimeout(() => {
    // Scroll the main window element
    window.scrollTo({ top: 0, left: 0, behavior: "instant" });

    // Fallback: If your page layout uses a scroll container (like .mainContainer), scroll it directly
    const mainContainer = document.querySelector(".mainContainer");
    if (mainContainer) {
      mainContainer.scrollTop = 0;
    }
  }, 10);
  const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.25,
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");

        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const hiddenElements = document.querySelectorAll(".animate-on-scroll");
  hiddenElements.forEach((el) => observer.observe(el));
});
</script>

<template>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Gochi+Hand&family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&family=Manrope:wght@200..800&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Permanent+Marker&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap"
    rel="stylesheet"
  />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Fraunces:ital,opsz,wght@0,9..144,100..900;1,9..144,100..900&family=Gochi+Hand&family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&family=Manrope:wght@200..800&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Permanent+Marker&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap"
    rel="stylesheet"
  />
  <div class="navBar">
    <div class="logoText">
      <img src="/sedateLogo.png" alt="" />
      <span>Sedate</span>
    </div>
    <div class="links">
      <button class="navBtns" @click="scrollToFive" href="/">
        How It Works
      </button>
      <button class="navBtns" @click="aboutUsScroll" href="/">About Us</button>
      <button class="navBtns" @click="questionsScroll" href="/">
        Your Questions
      </button>
    </div>
    <button class="navBarBook" @click="scrollToSection">
      Book Consultation
    </button>
  </div>
  <div class="mainContainer">
    <div class="hero">
      <span class="before">Before</span>
      <span class="during">During</span>
      <span class="after">After</span>
      <p>
        Everything your anesthesiologist wants you to know, explained like
        you're family.
      </p>
      <div class="heroBtn">
        <button @click="scrollToSection" class="heroDarkBtn">
          Schedule Your Consultation
        </button>
        <button @click="scrollToFive" class="heroLightBtn">How it Works</button>
      </div>
      <span class="scroll">Scroll to begin</span>
      <svg
        width="16"
        height="24"
        viewBox="0 0 16 24"
        fill="none"
        class="animate-bounce"
        aria-hidden="true"
      >
        <rect
          x="1"
          y="1"
          width="14"
          height="22"
          rx="7"
          stroke="currentColor"
          stroke-width="1.5"
        ></rect>
        <circle
          cx="8"
          cy="7"
          r="2.5"
          fill="currentColor"
          class="animate-float-slow"
        ></circle>
      </svg>
    </div>
    <div class="ticker-wrap">
      <div class="ticker-track">
        <!-- Group 1 -->
        <div class="ticker-group">
          <span>Written for Patients, Not Textbooks</span
          ><span class="dot">•</span> <span>12,000+ Consultations Guided</span
          ><span class="dot">•</span> <span>Every Phase Explained</span
          ><span class="dot">•</span> <span>Available 24 Hours</span
          ><span class="dot">•</span> <span>No Question Too Small</span
          ><span class="dot">•</span>
        </div>
        <!-- Group 2 (Exact Duplicate for the infinite loop effect) -->
        <div class="ticker-group" aria-hidden="true">
          <span>Written for Patients, Not Textbooks</span
          ><span class="dot">•</span> <span>12,000+ Consultations Guided</span
          ><span class="dot">•</span> <span>Every Phase Explained</span
          ><span class="dot">•</span> <span>Available 24 Hours</span
          ><span class="dot">•</span> <span>No Question Too Small</span
          ><span class="dot" ref="targetElementFive">•</span>
        </div>
      </div>
    </div>
    <div class="journey">
      <span class="fullPicture">The Full Picture</span>
      <h2>Five phases. Zero surprises.</h2>
      <p class="journeyDesc">
        We walk you through every stage of your anesthesia experience — from the
        first phone call to the moment you ask for crackers in recovery.
      </p>
      <div class="cards">
        <div class="cardOne">
          <!-- Left Column: Image wrapper for the decorative background shadow -->
          <div class="cardOneImageWrapper animate-on-scroll">
            <img src="/cardOne.png" alt="Anesthesiologist consultation" />
            <span class="phase-tag">Phase 01 — Consultation</span>
          </div>
          <div class="cardOneText animate-on-scroll">
            <p class="questionOne">"What will they actually ask me?"</p>
            <h3>Your first conversation with your anesthesiologist</h3>
            <p class="descOne">
              Before any procedure, a board-certified anesthesiologist reviews
              your full medical history — medications, allergies, prior
              surgeries, and the things you haven't mentioned yet because you
              weren't sure they mattered. They do matter. This conversation
              typically takes 20–30 minutes and shapes every decision made in
              the operating room.
            </p>
            <div class="warn">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="#5BA4B5"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="warn-icon"
                aria-hidden="true"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="8" x2="12" y2="12"></line>
                <line x1="12" y1="16" x2="12.01" y2="16"></line>
              </svg>
              <p class="warnDesc">
                Bring a list of all medications, including vitamins and
                supplements. Mention any family history of anesthesia reactions.
              </p>
            </div>
          </div>
        </div>
        <div class="cardTwo">
          <!-- Left Column: Image wrapper for the decorative background shadow -->
          <div class="cardTwoImageWrapper animate-on-scroll">
            <img src="/cardTwoImg.jpg" alt="Anesthesiologist consultation" />
            <span class="phaseTwo-tag">Phase 02 — Fasting Instructions</span>
          </div>
          <div class="cardTwoText animate-on-scroll">
            <p class="questionTwo">"Can I really not have coffee?"</p>
            <h3>Why nothing by mouth — and for exactly how long</h3>
            <p class="descTwo">
              The rule exists because a full stomach during anesthesia carries
              real risk. Modern guidelines are more nuanced than the old
              "nothing after midnight" rule: clear liquids are typically allowed
              up to 2 hours before, light meals up to 6 hours, and heavier meals
              up to 8 hours. Your anesthesiologist will give you exact times
              based on your specific procedure and start time.
            </p>
            <div class="warnTwo">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="#5BA4B5"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="warn-icon"
                aria-hidden="true"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="8" x2="12" y2="12"></line>
                <line x1="12" y1="16" x2="12.01" y2="16"></line>
              </svg>
              <p class="warnDescTwo">
                Clear liquids include water, apple juice, black coffee (no
                cream), and clear broth. Not orange juice. Not smoothies.
              </p>
            </div>
          </div>
        </div>
        <div class="cardOne">
          <!-- Left Column: Image wrapper for the decorative background shadow -->
          <div class="cardThreeImageWrapper animate-on-scroll">
            <img src="/cardThreeImg.png" alt="Anesthesiologist consultation" />
            <span class="phaseTwo-tag">Phase 03 — Pre-Op Hold</span>
          </div>
          <div class="cardOneText animate-on-scroll">
            <p class="questionOne">
              "What happens right before they take me in?"
            </p>
            <h3>The waiting room with warm blankets and an IV</h3>
            <p class="descOne">
              The pre-operative holding area is where your body and mind get
              their last preparation. A nurse places your IV — usually in the
              back of the hand or forearm. Vital signs are checked. Your
              surgical team introduces themselves. You'll receive
              pre-medications that begin relaxing your nervous system before you
              ever reach the operating room. Many patients say this is the
              moment their fear starts to ease.
            </p>
            <div class="warn">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="#5BA4B5"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="warn-icon"
                aria-hidden="true"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="8" x2="12" y2="12"></line>
                <line x1="12" y1="16" x2="12.01" y2="16"></line>
              </svg>
              <p class="warnDesc">
                You can ask for a warm blanket at any time. The nurses in pre-op
                have heard every question and will not rush you.
              </p>
            </div>
            <p class="cardThreeBtnText">
              Now that you know what a consultation covers —
            </p>
            <button class="cardThreeBtn">
              Schedule Your Pre-Anesthesia Consultation
            </button>
          </div>
        </div>
        <div class="cardTwo">
          <!-- Left Column: Image wrapper for the decorative background shadow -->
          <div class="cardFourImageWrapper animate-on-scroll">
            <img src="/cardFourImg.jpg" alt="Anesthesiologist consultation" />
            <span class="phaseTwo-tag">Phase 04 — Induction</span>
          </div>
          <div class="cardTwoText animate-on-scroll">
            <p class="questionTwo">
              "Will I count backwards? Will I feel anything?"
            </p>
            <h3>The moment anesthesia begins — what you will and won't feel</h3>
            <p class="descTwo">
              Induction is the transition from awake to unconscious. It happens
              in under 60 seconds. Most patients receive medication through
              their IV that feels like a cool rush up the arm, followed by a
              sensation of floating, then nothing. You will not be aware of the
              procedure. You will not feel pain. Awareness under anesthesia is
              extremely rare — occurring in roughly 1 in 19,000 cases — and your
              anesthesiologist monitors your depth continuously throughout.
            </p>
            <div class="warnTwo">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="#5BA4B5"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="warn-icon"
                aria-hidden="true"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="8" x2="12" y2="12"></line>
                <line x1="12" y1="16" x2="12.01" y2="16"></line>
              </svg>
              <p class="warnDescTwo">
                Your anesthesiologist stays in the room for your entire
                procedure. They are not doing something else.
              </p>
            </div>
          </div>
        </div>
        <div class="cardOne">
          <!-- Left Column: Image wrapper for the decorative background shadow -->
          <div class="cardOneImageWrapper animate-on-scroll">
            <img src="/cardFiveImg.png" alt="Anesthesiologist consultation" />
            <span class="phase-tag">Phase 05 — Recovery</span>
          </div>
          <div class="cardOneText animate-on-scroll">
            <p class="questionOne">
              "Why do I feel so disoriented when I wake up?"
            </p>
            <h3>Waking up: what's normal, what to expect, when to speak up</h3>
            <p class="descOne">
              The recovery room — called the PACU — is where anesthesia is
              carefully reversed. Waking up can feel slow and strange. You may
              feel cold, confused, or emotional. Nausea is common and treatable.
              Nurses monitor your oxygen, blood pressure, and pain level every
              few minutes. Most patients are transferred to a regular room or
              discharged within 1–2 hours, depending on the procedure.
            </p>
            <div class="warn">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="#5BA4B5"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="warn-icon"
                aria-hidden="true"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="8" x2="12" y2="12"></line>
                <line x1="12" y1="16" x2="12.01" y2="16"></line>
              </svg>
              <p class="warnDesc" ref="targetAbout">
                Tell your recovery nurse immediately if you feel nauseous, have
                unusual pain, or feel like something is wrong. There is no wrong
                answer.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="darkBg">
      <div class="medicalContainer">
        <div class="left animate-on-scroll">
          <span>Written by doctors</span>
          <h2 class="leftTitleOne">Every word here was written</h2>
          <h2 class="leftTitleTwo">by an anesthesiologist.</h2>
        </div>
        <div class="right animate-on-scroll">
          <p class="rightDesc">
            Not a content team. Not a medical writer working from a textbook.
            The physicians who wrote these pages are the same physicians who
            will stand beside you in the operating room — and they wrote what
            they wish every patient already knew walking in.
          </p>
        </div>
      </div>
      <div class="fourCardsContainer animate-on-scroll">
        <div class="surgery">
          <span class="text-2xl mb-3 block" role="img" aria-hidden="true"
            >🫀</span
          >
          <p class="main">12,000+</p>
          <p class="small">Pre-surgery consultations guided</p>
        </div>
        <div class="average">
          <span class="text-2xl mb-3 block" role="img" aria-hidden="true"
            >🩺</span
          >
          <p class="main">18 yrs</p>
          <p class="small">Average anesthesiologist experience</p>
        </div>
        <div class="satisfaction">
          <span class="text-2xl mb-3 block" role="img" aria-hidden="true"
            >⭐</span
          >
          <p class="main">99.7%</p>
          <p class="small">Patient satisfaction in post-op surveys</p>
        </div>
        <div class="education">
          <span class="text-2xl mb-3 block" role="img" aria-hidden="true"
            >🌙</span
          >
          <p class="main">24 / 7</p>
          <p class="small">Educational content available</p>
        </div>
      </div>
      <p class="credits animate-on-scroll">Credentials & Affiliations</p>
      <div class="fourCardCredits animate-on-scroll">
        <span>American Board of Anesthesiology Certified</span>
        <span>Society for Pediatric Anesthesia Members</span>
        <span>American Society of Anesthesiologists</span>
        <span>Joint Commission Accredited Practices</span>
      </div>
      <div class="reviewContainer animate-on-scroll">
        <div class="review">
          <svg
            width="32"
            height="24"
            viewBox="0 0 32 24"
            fill="#5BA4B5"
            class="mb-4 opacity-60"
            aria-hidden="true"
          >
            <path
              d="M0 24V14.4C0 6.4 5.333 1.6 16 0l1.6 2.4C12.267 3.6 9.2 6 8.4 9.6H14V24H0zm18 0V14.4C18 6.4 23.333 1.6 34 0L35.6 2.4C30.267 3.6 27.2 6 26.4 9.6H32V24H18z"
            ></path>
          </svg>
          <p class="reviewDesc">
            “ The single most effective thing we can do to reduce patient
            anxiety is explain exactly what will happen — in plain language,
            before it happens. An informed patient is a calmer patient. A calmer
            patient recovers faster. ”
          </p>
          <div class="doctor">
            <div class="DR">DR</div>
            <div class="doctorDesc">
              <p class="DrName">Dr. Rachel Okafor, MD</p>
              <p class="DrRank">
                Board-Certified Anesthesiologist, Founder of Sedate
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="questions" ref="questionsTarget">
      <div class="questionsleft animate-on-scroll">
        <span>Patient Questions</span>
        <h2>The questions patients ask at 2 AM.</h2>
        <p class="questionleftDesc">
          These are the real searches patients make the night before surgery. We
          answer them plainly, without softening the truth or hiding behind
          medical language.
        </p>
        <div class="questionBtn">
          <p class="questionBtnTitle">Still have a question?</p>
          <p class="text-sm">
            Your consultation is the place to ask anything — including the
            things on this list.
          </p>
          <button>Book a consultation</button>
        </div>
      </div>
      <div class="questionRight animate-on-scroll">
        <div class="faq-container">
          <div
            v-for="(item, index) in faqItems"
            :key="index"
            class="faq-item"
            :class="{ 'is-open': activeIndex === index }"
          >
            <!-- Clickable Header Row -->
            <div class="faq-header" @click="toggleItem(index)">
              <div class="faq-left-meta">
                <span class="faq-tag">{{ item.tag }}</span>
              </div>

              <h4 class="faq-question">{{ item.question }}</h4>

              <div class="faq-trigger">
                <div class="circle-btn">
                  <span class="line horizontal"></span>
                  <span class="line vertical"></span>
                </div>
              </div>
            </div>

            <!-- Smooth Collapsible Content Container -->
            <div class="faq-body">
              <div class="faq-content">
                <p>{{ item.answer }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="book" ref="targetElement">
      <!-- Header Section -->
      <div class="bookTitle">
        <span>Next Step</span>
        <h2>Schedule Your Pre-Anesthesia Consultation</h2>
        <p>
          A 30-minute conversation that answers everything you've been afraid to
          ask — before the day you need the answers most.
        </p>
      </div>

      <!-- Form Section -->
      <div class="form-wrapper">
        <div class="form-card">
          <h2 class="form-title">Tell us about your procedure</h2>

          <!-- WIRED: Triggers handleFormSubmit on submission -->
          <form @submit.prevent="handleFormSubmit">
            <!-- Row 1: Dropdown -->
            <div class="form-group">
              <label>PROCEDURE TYPE *</label>
              <!-- WIRED v-model -->
              <select v-model="form.procedureType" required>
                <option value="" disabled selected>
                  Select your procedure type
                </option>
                <option>General Surgery</option>
                <option>Orthopedic Surgery</option>
                <option>Pediatric Surgery</option>
                <option>Cardiac Surgery</option>
                <option>Dental / Oral Surgery</option>
                <option>Other / Not Sure Yet</option>
              </select>
            </div>

            <!-- Row 2: Name & Email -->
            <div class="form-grid-row">
              <div class="form-group">
                <label>YOUR NAME *</label>
                <!-- WIRED v-model -->
                <input
                  type="text"
                  v-model="form.name"
                  placeholder="Margaret Hollis"
                  required
                />
              </div>
              <div class="form-group">
                <label>EMAIL ADDRESS *</label>
                <!-- WIRED v-model -->
                <input
                  type="email"
                  v-model="form.email"
                  placeholder="margaret@email.com"
                  required
                />
              </div>
            </div>

            <!-- Row 3: Phone & Date -->
            <div class="form-grid-row">
              <div class="form-group">
                <label>PHONE (OPTIONAL)</label>
                <!-- WIRED v-model -->
                <input
                  type="tel"
                  v-model="form.phone"
                  placeholder="(555) 000-0000"
                />
              </div>
              <div class="form-group">
                <label>PREFERRED DATE RANGE *</label>
                <!-- WIRED v-model -->
                <input
                  type="text"
                  v-model="form.dateRange"
                  placeholder="e.g. March 10–20, 2026"
                  required
                />
              </div>
            </div>

            <!-- Row 4: Textarea -->
            <div class="form-group">
              <label>WHAT CONCERNS YOU MOST ABOUT ANESTHESIA?</label>
              <!-- WIRED v-model -->
              <textarea
                v-model="form.concerns"
                rows="4"
                placeholder="There's no wrong answer here. Write whatever is on your mind — we read every response."
              ></textarea>
              <span class="helper-text"
                >Naming the fear is the first step past it.</span
              >
            </div>

            <!-- WIRED: Button state alters dynamically while handling email requests -->
            <button
              type="submit"
              class="submit-btn"
              :disabled="isSubmitting || isSuccess"
            >
              <template v-if="isSubmitting">Sending Details...</template>
              <template v-else-if="isSuccess">Sent !</template>
              <template v-else>Schedule My Consultation &rarr;</template>
            </button>

            <p class="footer-note">
              No credit card required. We'll confirm your appointment by email
              within one business day.
            </p>
          </form>
        </div>
        <!-- Info Card Container (Properly aligned under the main form) -->
        <div class="info-card-container">
          <div class="info-card">
            <h3>What to expect after you submit</h3>
            <ul class="expect-list">
              <li>
                <span class="checkmark">&#10003;</span>
                <p>
                  A board-certified anesthesiologist reviews your form
                  personally
                </p>
              </li>
              <li>
                <span class="checkmark">&#10003;</span>
                <p>
                  We call or email within one business day to confirm your time
                </p>
              </li>
              <li>
                <span class="checkmark">&#10003;</span>
                <p>Your consultation is 30 minutes, by video or phone</p>
              </li>
              <li>
                <span class="checkmark">&#10003;</span>
                <p>
                  You can reschedule up to 24 hours before, no questions asked
                </p>
              </li>
            </ul>
          </div>

          <!-- Card 2: Urgent notice callout box -->
          <div class="urgent-notice-box">
            <p>
              <strong>Surgery in the next 48 hours?</strong> Call your
              hospital's anesthesiology department directly. This form is for
              scheduled consultations only.
            </p>
          </div>
        </div>
      </div>
    </div>
    <footer class="site-footer">
      <div class="footer-container">
        <!-- Left: Logo & Copyright -->
        <div class="footer-left">
          <div class="footer-logo">
            <strong>Sedate</strong>
          </div>
          <span class="copyright">© 2026 Sedate Health, Inc.</span>
        </div>

        <!-- Center: Links -->
        <div class="footer-center">
          <a href="#">Privacy</a>
          <a href="#">Terms</a>
          <a href="#">Accessibility</a>
          <a href="#">Contact</a>
        </div>

        <!-- Right: Social Icons -->
        <div class="footer-right">
          <!-- X (formerly Twitter) SVG Icon -->
          <a href="#" class="social-icon" aria-label="X (Twitter)">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
              <path
                d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"
              />
            </svg>
          </a>
          <!-- LinkedIn SVG Icon -->
          <a href="#" class="social-icon" aria-label="LinkedIn">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
              <path
                d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"
              />
            </svg>
          </a>
        </div>
      </div>

      <!-- Bottom Medical Advice Disclaimer Row -->
      <div class="footer-disclaimer">
        <p>
          This site is for educational purposes only. It does not constitute
          medical advice. Always consult your care team before any procedure.
        </p>
      </div>
    </footer>
  </div>
</template>

<style>
html,
body {
  margin: 0;
  padding: 0;
}
</style>

<style scoped>
@keyframes scrollTicker {
  0% {
    transform: translate3d(0, 0, 0);
  }
  100% {
    /* Moves exactly half the width of the entire track */
    transform: translate3d(-50%, 0, 0);
  }
}

@keyframes appear {
  from {
    opacity: 0;
    transform: translateY(300px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes enterLeft {
  from {
    opacity: 0;
    transform: translateX(-100px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes enterRight {
  from {
    opacity: 0;
    transform: translateX(100px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.mainContainer {
  width: 100%;
  height: 100%;
  background-color: #f7fafc;
  overflow-x: hidden;
}

.navBar {
  display: flex;
  flex-direction: row;
  height: 10%;
  justify-content: space-around;
  align-items: center;
  padding: 16px 32px;
  position: sticky;
  top: 0;
  z-index: 1000;
  background-color: #ffffff;
  /* margin-bottom: 2rem; */
  img {
    width: 20%;
  }
}

.links {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
}

.links a {
  text-decoration: none;
  font-family: "DM Sans", sans-serif;
  color: rgba(74, 85, 104, 1);
  font-weight: 500;
  font-size: 0.875rem;
  line-height: 1.25rem;
  transition: 0.2s;
}

.navBtns:hover {
  color: rgba(91, 164, 181, 1);
}

.logoText {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 10%;
}

.logoText span {
  font-family: "DM Sans", sans-serif;
  font-weight: 600;
  font-size: 1.25rem;
  line-height: 1.75rem;
  color: rgba(74, 85, 104, 1);
}

.navBarBook {
  font-family: "DM Sans", sans-serif;
  background-color: #5ba4b5;
  color: #fff;
  font-size: 0.875rem;
  letter-spacing: 0.02rem;
  padding: 0.85rem 2rem;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
  transition: 0.4s ease;
  font-weight: 600;
}

.navBtns {
  border: none;
  background: #fff;
  /* font-family: "'DM SANS'", sans-serif; */
  text-decoration: none;
  font-family: "DM Sans", sans-serif;
  color: rgba(74, 85, 104, 1);
  font-weight: 500;
  font-size: 0.875rem;
  line-height: 1.25rem;
  transition: 0.2s;
  cursor: pointer;
}

.navBarBook:hover {
  background-color: #4a8fa0;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(91, 164, 181, 0.35);
}

.hero {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.before,
.during {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 12vw;
  font-family: "Fraunces", serif;
  text-transform: uppercase;
  font-weight: 500;
  color: #4a5568;
  letter-spacing: -0.04rem;
  line-height: 0.9;
  font-weight: 400;
  width: 50%;
  margin: 10px 0;
  border-bottom: 1px solid #cbd5e0;
}

.before {
  animation: appear 1s ease-in-out;
  animation-duration: 1s;
  animation-fill-mode: backwards;
}

.during {
  animation: appear 1s ease-in-out;
  animation-delay: 0.7s;
  animation-fill-mode: backwards;
}

.after {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 12vw;
  font-family: "Fraunces", serif;
  color: #5ba4b5;
  font-weight: 700;
  text-transform: uppercase;
  /* letter-spacing: -0.04em; */
  line-height: 0.9;
  width: 60%;
  margin-bottom: 2rem;
}

.after {
  animation: appear 1.1s ease-in-out;
  animation-delay: 1s;
  animation-fill-mode: backwards;
}

.hero p {
  display: block;
  text-align: center;
  font-style: italic;
  font-family: "DM Sans", sans-serif;
  font-size: 1.25rem;
  line-height: 1.75rem;
  color: rgba(74, 85, 104, 1);
  font-weight: 400;
  width: 35%;
  animation: appear 1s ease-in-out;
  animation-delay: 1.1s;
  animation-fill-mode: backwards;
}

.heroBtn {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
  gap: 0.5rem;
  margin-bottom: 30px;
}

.heroDarkBtn {
  background-color: #5ba4b5;
  color: #fff;
  font-size: 0.875rem;
  letter-spacing: 0.02em;
  padding: 0.85rem 2rem;
  font-weight: 600;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
  transition: all 0.4s ease;
}

.heroDarkBtn:hover {
  background-color: #4a8fa0;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(91, 164, 181, 0.35);
}

.heroLightBtn {
  display: inline-flex;
  align-items: center;
  background: transparent;
  color: #5ba4b5;
  font-weight: 600;
  font-size: 0.875rem;
  padding: 0.85rem 2rem;
  border-radius: 0.5rem;
  border: 1.5px solid #5ba4b5;
  cursor: pointer;
  transition: all 0.4s ease;
}

.heroLightBtn:hover {
  background-color: #5ba4b5;
  color: #fff;
  transform: translateY(-2px);
}

.ticker-wrap {
  width: 100%;
  overflow: hidden;
  background-color: rgb(235 244 251 /1);
  padding: 15px 0;
  border-top: 1px solid #e2e8f0;
  border-bottom: 1px solid #e2e8f0;
  margin-bottom: 112px;
}

/* 2. The track houses both groups side-by-side and handles the animation */
.ticker-track {
  display: flex;
  width: max-content;
  animation: scrollTicker 30s linear infinite;
}

/* 3. Style the individual groups and spacing */
.ticker-group {
  display: flex;
  align-items: center;
  justify-content: space-around;
  white-space: nowrap;
  padding-right: 20px; /* Gives a tiny bit of buffer space between loops */
}

.ticker-group span {
  font-family: sans-serif;
  color: #4a5568;
  font-size: 16px;
  margin: 0 25px; /* Spacing between the text and the dots */
}

/* The blue dot separator */
.ticker-group .dot {
  color: #3182ce;
  font-weight: bold;
}

.scroll {
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-weight: 500;
  font-size: 0.75rem;
  font-family: "DM Sans", sans-serif;
  line-height: 1rem;
  color: rgb(160 174 192 / 1);
  margin-bottom: 8px;
}

svg {
  color: rgb(160 174 192 / 1);
}

.animate-bounce {
  margin-bottom: 80px;
}

.journey {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.fullPicture {
  font-weight: 600;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #5ba4b5;
  background-color: rgba(91, 164, 181, 0.1);
  border: 1px solid rgba(91, 164, 181, 0.25);
  padding: 0.3rem 0.8rem;
  font-family: "DM Sans", sans-serif;
  border-radius: 999px;
}

.journey h2 {
  letter-spacing: -0.02em;
  font-size: 3rem;
  line-height: 1;
  font-family: "Fraunces", serif;
  font-weight: 600;
  color: rgb(45 55 72 /1);
  margin-bottom: 1rem;
}

.journeyDesc {
  color: rgb(113 128 150 / 1);
  line-height: 1.625;
  font-size: 1.125rem;
  width: 60%;
  font-family: "DM Sans", sans-serif;
  text-align: center;
}

.questionOne {
  color: rgb(113 128 150 /1);
  font-family: "DM Sans", sans-serif;
  text-align: left;
  line-height: 1.625;
  font-size: 1.125rem;
  width: 100%;
  font-size: 1.25rem;
  line-height: 1.75rem;
  color: rgb(91 164 181 / 1);
  font-family: "Fraunces", serif;
  font-style: italic;
}

.cards {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  padding: 60px 20px;
  flex-direction: column;
}

.cardOne {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 100%;
  max-width: 1100px;
  gap: 80px; /* Generous gap between image and text like the screenshot */
}

/* Image Column */
.cardOneImageWrapper {
  position: relative;
  width: 40%;
  opacity: 0;
  will-change: opacity, transform;
}

.cardOneImageWrapper.is-visible {
  animation: enterLeft 0.8s ease forwards; /* 'forwards' keeps it visible at the end */
}

.cardOne img {
  width: 100%;
  height: auto;
  border-radius: 24px;
  display: block;
  /* Recreates the soft outer glow behind the image in the screenshot */
  box-shadow:
    -20px -20px 0px rgba(91, 164, 181, 0.05),
    0 20px 40px rgba(0, 0, 0, 0.08);
}

.phase-tag {
  position: absolute;
  bottom: 20px;
  left: 20px;
  background: rgba(91, 164, 181, 0.1);
  backdrop-filter: blur(8px);
  color: #5ba4b5;
  font-family: "DM Sans", sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 6px 14px;
  border: 1px solid rgba(91, 164, 181, 0.25);
  border-radius: 999px;
}

/* Text Column */
/* Update this block to include text-align: left !important */
.cardOneText {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 50%;
  text-align: left !important; /* Forces the block itself to read left */
  opacity: 0;
  will-change: opacity, transform;
}

.cardOneText.is-visible {
  animation: enterRight 0.8s ease forwards; /* 'forwards' keeps it visible at the end */
}

/* Explicitly force your paragraph and heading elements to left-align */
.questionOne,
.cardOneText h3,
.descOne {
  text-align: left;
  width: 100%; /* Ensures they fill the container width and don't shrink wrap */
}

.cardOneText h3 {
  font-size: 1.875rem;
  line-height: 1.75rem;
  color: rgb(45 55 72 / 1);
  font-family: "Fraunces", serif;
  font-weight: 600;
  margin: 0;
}

.descOne {
  font-size: 1.125rem;
  line-height: 1.75rem;
  color: rgb(74 85 104 / 1);
  font-family: "DM Sans", sans-serif;
}

/* Fix the text styling inside your warning alert block */
.warn {
  display: flex;
  flex-direction: row;
  align-items: center; /* Vertically centers the icon with the text */
  justify-content: flex-start; /* Keeps items pushed to the left */
  gap: 12px;
  background-color: #ebf4fb;
  border: 1px solid rgba(91, 164, 181, 0.2);
  padding: 16px 20px;
  border-radius: 12px;
  width: 100%;
  text-align: left; /* Breaks any inherited centering */
}

.warnDesc {
  font-family: "DM Sans", sans-serif;
  color: rgb(74 85 104 / 1);
  font-size: 0.95rem;
  line-height: 1.5;
  margin: 0;
  text-align: left;
}

.cardTwo {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row-reverse;
  background-color: rgb(235 244 251 / 1);
  padding: 96px 0;
  margin-top: 96px;
  gap: 80px;
  margin-bottom: 96px;
}

.cardTwoImageWrapper {
  position: relative;
  width: 35%;
  opacity: 0;
  will-change: opacity, transform;
}

.cardTwoImageWrapper.is-visible {
  animation: enterRight 0.8s ease forwards;
}

.cardTwoImageWrapper img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 24px;
}

.cardTwoText {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 40%;
  opacity: 0;
  text-align: left;
  will-change: opacity, transform;
}

.cardTwoText.is-visible {
  animation: enterLeft 0.8s ease forwards;
}

.questionTwo {
  color: rgb(113 128 150 /1);
  font-family: "DM Sans", sans-serif;
  text-align: left;
  line-height: 1.625;
  font-size: 1.125rem;
  width: 100%;
  font-size: 1.25rem;
  line-height: 1.75rem;
  color: rgb(91 164 181 / 1);
  font-family: "Fraunces", serif;
  font-style: italic;
  text-align: left;
}

.cardTwoText h3 {
  font-size: 1.875rem;
  line-height: 2.25rem;
  color: rgb(45 55 72 / 1);
  font-family: "Fraunces", serif;
  font-weight: 600;
  margin: 0;
  width: 100%;
  text-align: left;
  letter-spacing: -0.02em;
}

.descTwo {
  font-size: 1.125rem;
  line-height: 1.75rem;
  color: rgb(74 85 104 / 1);
  font-family: "DM Sans", sans-serif;
}

.phaseTwo-tag {
  position: absolute;
  bottom: 20px;
  left: 20px;
  background: rgba(91, 164, 181, 0.1);
  backdrop-filter: blur(8px);
  color: #5ba4b5;
  font-family: "DM Sans", sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 6px 14px;
  border: 1px solid rgba(91, 164, 181, 0.25);
  border-radius: 999px;
}

.warnTwo {
  display: flex;
  flex-direction: row;
  align-items: center; /* Vertically centers the icon with the text */
  justify-content: flex-start; /* Keeps items pushed to the left */
  gap: 12px;
  background-color: #ebf4fb;
  border: 1px solid rgba(91, 164, 181, 0.2);
  padding: 30px 20px;
  border-radius: 12px;
  width: 86%;
  height: auto; /* Changed from 5vh to auto for responsiveness */
  text-align: left; /* Breaks any inherited centering */
  background-color: rgba(91, 164, 181, 0.08);
}

.warnDescTwo {
  font-family: "DM Sans", sans-serif;
  color: rgb(74 85 104 / 1);
  font-size: 0.95rem;
  line-height: 1.5;
  margin: 0;
  text-align: left;
}

.warnTwo svg {
  width: 9%;
  min-width: 24px;
}

.cardThreeImageWrapper {
  position: relative;
  width: 38%;
  opacity: 0;
  will-change: opacity, transform;
}

.cardThreeImageWrapper.is-visible {
  animation: enterLeft 1s ease forwards;
}

.cardThreeBtnText {
  margin-top: 24px;
  color: rgb(113 128 150 / 1);
  font-size: 0.875rem;
  line-height: 1.25rem;
  font-family: "DM Sans", sans-serif;
}

.cardThreeBtn {
  background-color: #5ba4b5;
  color: #fff;
  font-size: 0.875rem;
  letter-spacing: 0.02em;
  padding: 0.85rem 2rem;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
  transition: 0.3s ease;
}

.cardThreeBtn:hover {
  background-color: #4a8fa0;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(91, 164, 181, 0.35);
}

.cardFourImageWrapper {
  position: relative;
  width: 35%;
  opacity: 0;
  will-change: opacity, transform;
}

.cardFourImageWrapper img {
  width: 70%;
  height: auto;
  display: block;
  border-radius: 24px;
}

.cardFourImageWrapper.is-visible {
  animation: enterRight 1s ease forwards;
}

.darkBg {
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* align-items: center; */
  background-color: rgb(45 55 72 / 1);
}

.medicalContainer {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
}

.left {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  margin: 0 20px;
  flex-direction: column;
  opacity: 0;
  will-change: opacity, transform;
}

.left.is-visible {
  animation: enterLeft 0.8s ease forwards;
}

.left span {
  display: inline-flex;
  align-items: center;
  font-weight: 600;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #5ba4b5;
  background-color: rgba(91, 164, 181, 0.1);
  border: 1px solid rgba(91, 164, 181, 0.25);
  padding: 0.3rem 0.8rem;
  border-radius: 999px;
  font-family: "DM Sans", sans-serif;
  margin-top: 50px;
}

.leftTitleOne {
  letter-spacing: -0.02em;
  font-size: 3rem;
  line-height: 1;
  color: #fff;
  font-family: "Fraunces", serif;
  font-weight: 600;
  width: 80%;
}

.leftTitleTwo {
  margin-top: -40px;
  letter-spacing: -0.02em;
  font-size: 3rem;
  line-height: 1;
  color: rgb(91 164 181 / 1);
  font-family: "Fraunces", serif;
  font-weight: 600;
}

.right {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 80px;
  width: 50%;
  height: 100%;
  opacity: 0;
  will-change: opacity, transform;
}

.right.is-visible {
  animation: enterRight 0.8s ease forwards;
}

.right p {
  color: rgb(160 174 192 / 1);
  line-height: 1.625;
  font-size: 1.125rem;
  font-family: "DM Sans", sans-serif;
  width: 70%;
}

.fourCardsContainer {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  flex-direction: row;
  margin-top: 64px;
  margin-bottom: 4rem;
  opacity: 0;
  will-change: opacity, transform;
}

.fourCardsContainer.is-visible {
  animation: appear 0.8s ease forwards;
}

.surgery,
.average,
.satisfaction,
.education {
  display: flex;
  background-color: #fff;
  border-radius: 16px;
  margin-bottom: 20px;
  align-items: flex-start;
  justify-content: center;
  flex-direction: column;
  padding: 28px 24px;
  width: 15%;
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.surgery:hover,
.average:hover,
.satisfaction:hover,
.education:hover {
  background-color: hsla(0, 0%, 100%, 0.08);
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(74, 85, 104, 0.1);
  border: 1px solid #cbd5e0;
}

.surgery span,
.average span,
.satisfaction span,
.education span {
  font-size: 1.5rem;
  line-height: 2rem;
}

.main {
  letter-spacing: -0.03em;
  font-size: 2.25rem;
  line-height: 2.5rem;
  font-family: Fraunces, serif;
  font-weight: 700;
  margin-bottom: -8px;
  color: rgb(91 164 181 / 1);
  margin-top: 10px;
}

.small {
  line-height: 1.625;
  font-family: "DM Sans", sans-serif;
  font-size: 0.75rem;
  color: rgb(160 174 192 / 1);
  margin-bottom: 0;
}

.fourCardCredits {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  flex-direction: row;
  margin-bottom: 64px;
  opacity: 0;
  will-change: opacity, transform;
}

.fourCardCredits.is-visible {
  animation: appear 0.8s ease forwards;
}

.fourCardCredits span {
  color: rgb(203 213 224 / 1);
  font-weight: 500;
  font-size: 0.75rem;
  line-height: 1rem;
  padding: 0.5rem 1rem;
  background-color: hsla(0, 0%, 100%, 0.07);
  border: 1px solid hsla(0, 0%, 100%, 0.12);
  border-radius: 999px;
  font-family: "DM Sans", sans-serif;
}

.credits {
  color: rgb(113 128 150 / 1);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 0.75rem;
  line-height: 1rem;
  font-family: "DM Sans", sans-serif;
  margin-left: 80px;
  opacity: 0;
  will-change: opacity, transform;
  margin-bottom: 24px;
}

.credits.is-visible {
  animation: appear 0.8s ease forwards;
}

.reviewContainer {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 112px;
  opacity: 0;
  will-change: opacity, transform;
}

.reviewContainer.is-visible {
  animation: appear 0.8s ease forwards;
}

.review {
  background-color: rgba(91, 164, 181, 0.12);
  border: 1px solid rgba(91, 164, 181, 0.25);
  border-radius: 1rem;
  padding: 2.5rem;
  width: 70%;
}

.reviewDesc {
  font-size: 1.5rem;
  line-height: 2rem;
  font-family: "Fraunces", serif;
  color: #fff;
  font-weight: 300;
}

.doctor {
  display: flex;
  gap: 20px;
  align-items: center;
  flex-direction: row;
}

.DR {
  display: flex;
  justify-content: center;
  align-items: center;
  color: rgb(91 164 181 /1);
  border-radius: 9999px;
  background-color: rgba(91, 164, 181, 0.3);
  font-size: 0.875rem;
  height: 2.5rem;
  line-height: 1.25rem;
  font-weight: 700;
  width: 2.5rem;
}

.DrName {
  color: rgb(255 255 255 / 1);
  font-weight: 600;
  font-size: 0.875rem;
  line-height: 1.25rem;
  font-family: "DM Sans", sans-serif;
  margin-bottom: -12px;
}

.DrRank {
  color: rgb(113 128 150 / 1);
  font-weight: 600;
  font-size: 0.75rem;
  line-height: 1rem;
  font-family: "DM Sans", sans-serif;
}

.questions {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  width: 100%;
  padding: 112px 64px 112px 32px;
  background-color: rgb(235 244 251 / 1);
  flex-direction: row;
  box-sizing: border-box;
  /* gap: 20px; */
}

.questionsleft {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  /* padding-left: 2rem; */
  flex-direction: column;
  opacity: 0;
  will-change: opacity, transform;
  margin-right: -500px;
}

.questionsleft.is-visible {
  animation: enterLeft 0.8s ease forwards;
}

.questionsleft span {
  display: inline-flex;
  align-items: center;
  font-weight: 600;
  gap: 0.4rem;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #5ba4b5;
  background: rgba(91, 164, 181, 0.1);
  border: 1px solid rgba(91, 164, 181, 0.25);
  padding: 0.3rem 0.8rem;
  border-radius: 999px;
  font-family: "DM Sans", sans-serif;
}

.questionsleft h2 {
  letter-spacing: -0.02em;
  font-size: 2.25rem;
  line-height: 2.5rem;
  font-family: "Fraunces", serif;
  color: rgb(45 55 72 / 1);
  font-weight: 600;
  width: 42%;
}

.questionleftDesc {
  color: rgb(113 128 150 / 1);
  line-height: 1.625;
  font-size: 1rem;
  font-family: "DM Sans", sans-serif;
  width: 40%;
}

.questionBtn {
  background-color: rgb(255 255 255 / 1);
  width: 35%;
  border-radius: 16px;
  padding: 1.25rem;
  border: 1px solid rgb(203 213 224 / 1);
  box-sizing: border-box;
}

.questionBtn button {
  font-family: "DM Sans", sans-serif;
  background-color: #5ba4b5;
  color: #fff;
  font-size: 0.875rem;
  letter-spacing: 0.02rem;
  padding: 0.85rem 2rem;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
  width: 100%;
  transition: 0.4s ease;
  font-weight: 600;
}

.questionBtn button:hover {
  background: #4a8fa0;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(91, 164, 181, 0.35);
}

.questionBtnTitle {
  font-size: 0.9rem;
  line-height: 1.25rem;
  color: rgb(45 55 72 / 1);
  font-weight: 900;
  font-family: "DM Sans", sans-serif;
}

.questionRight {
  width: 60%;
  /* height: 1%; */
  margin: 0 64px 0 0;
  opacity: 0;
  will-change: opacity, transform;
}

.questionRight.is-visible {
  animation: enterRight 0.8s ease forwards;
}

.text-sm {
  color: rgb(113 128 150 /1);
  font-size: 0.875rem;
  font-family: "DM Sans", sans-serif;
  line-height: 1.25rem;
  width: 100%;
}

.faq-container {
  width: 100%;
  max-width: 1000px;
  margin: 40px auto;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
  overflow: hidden;
}

.faq-item {
  border-bottom: 1px solid #e2e8f0;
  transition: background-color 0.3s ease;
}

.faq-item:last-child {
  border-bottom: none;
}

/* Header styling layout grids */
.faq-header {
  display: flex;
  align-items: center;
  padding: 16px 32px; /* Fixed from 5px to give balanced spacing */
  cursor: pointer;
  user-select: none;
  gap: 24px;
}

.faq-header:hover {
  background-color: rgba(235, 244, 251, 0.3);
}

/* Left Category Pill Badge */
.faq-left-meta {
  width: 15%;
  flex-shrink: 0;
}

.faq-tag {
  display: inline-block;
  font-family: "DM Sans", sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #5ba4b5;
  background-color: rgba(91, 164, 181, 0.1);
  padding: 4px 12px;
  border-radius: 6px;
  margin-right: 20px;
}

/* Middle Question Styling */
.faq-question {
  flex-grow: 1;
  font-family: "DM Sans", sans-serif;
  font-size: 1.2rem;
  font-weight: 500;
  color: #2d3748;
  margin-left: 20px;
  text-align: left;
  transition: color 0.2s ease;
}

.faq-item.is-open .faq-question {
  color: #5ba4b5; /* Highlight question text color when open */
}

/* Right Side Interactive Expanding Circular Plus Indicator */
.faq-trigger {
  flex-shrink: 0;
}

.circle-btn {
  position: relative;
  width: 32px;
  height: 32px;
  border: 1px solid #cbd5e0;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.faq-item.is-open .circle-btn {
  background-color: #5ba4b5;
  border-color: #5ba4b5;
  transform: rotate(90deg); /* Beautiful rotate transition effect */
}

.line {
  position: absolute;
  background-color: #a0aec0;
  transition:
    background-color 0.3s ease,
    transform 0.3s ease;
}

.faq-item.is-open .line {
  background-color: #ffffff; /* Turns cross elements white when open */
}

.horizontal {
  width: 14px;
  height: 1.5px;
}

.vertical {
  width: 1.5px;
  height: 14px;
}

/* Magic line-collapse animation converts Plus to Minus perfectly */
.faq-item.is-open .vertical {
  transform: scaleY(0);
}

/* Pure CSS Variable-Height Transition Trick using CSS Grid Row fractionals */
.faq-body {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.faq-item.is-open .faq-body {
  grid-template-rows: 1fr;
}

.faq-content {
  overflow: hidden;
}

.faq-content p {
  font-family: "DM Sans", sans-serif;
  font-size: 1.05rem;
  line-height: 1.65;
  color: #718096;
  margin: 0;
  padding: 0 32px 32px calc(15% + 56px); /* Indents paragraph directly under the question title line */
}

/* 1. Wrap the entire element section in a flex column layout */
.book {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  background-color: #f7fafc;
  padding-bottom: 80px;
  box-sizing: border-box;
}

.bookTitle {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
  text-align: center;
  padding: 0 20px;
  box-sizing: border-box;
}

.bookTitle span {
  display: inline-flex;
  align-items: center;
  font-weight: 600;
  gap: 0.4rem;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #5ba4b5;
  background: rgba(91, 164, 181, 0.1);
  border: 1px solid rgba(91, 164, 181, 0.25);
  padding: 0.3rem 0.8rem;
  border-radius: 999px;
  margin-top: 5rem;
  font-family: "DM Sans", sans-serif;
}

.bookTitle h2 {
  font-size: 2.7rem;
  line-height: 1.2;
  font-family: "Fraunces", serif;
  color: #2d3748;
  font-weight: 600;
  margin-top: 20px;
  margin-bottom: 16px;
}

.bookTitle p {
  line-height: 1.625;
  font-size: 1.125rem;
  color: #718096;
  width: 100%;
  max-width: 500px;
  text-align: center;
  margin-bottom: 24px;
}

.form-wrapper {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  width: 100%;
  padding: 20px;
  gap: 60px; /* Reduced from 120px to display better on medium screens */
  box-sizing: border-box;
}

.form-card {
  width: 100%;
  max-width: 600px;
  background: #ffffff;
  padding: 40px;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  box-sizing: border-box;
}

.form-card h2.form-title {
  font-family: "Fraunces", serif;
  color: rgb(45 55 72 / 1);
  font-weight: 600;
  margin-top: 0;
  margin-bottom: 32px;
  font-size: 1.25rem;
  line-height: 1.75rem;
  text-align: left;
}

.form-grid-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.form-group {
  margin-bottom: 24px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

label {
  font-family: "DM Sans", sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  color: #4a5568;
  letter-spacing: 0.05em;
  margin-bottom: 8px;
}

input,
select,
textarea {
  width: 100%;
  box-sizing: border-box;
  padding: 14px;
  border: 1px solid #cbd5e0;
  border-radius: 8px;
  font-size: 1rem;
  color: #4a5568;
  font-family: "DM Sans", sans-serif;
  background-color: #fff;
}

textarea {
  resize: vertical;
}

.helper-text {
  font-size: 0.85rem;
  color: #a0aec0;
  margin-top: 8px;
}

.submit-btn {
  width: 100%;
  background-color: #5ba4b5;
  color: white;
  padding: 16px;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  margin-top: 10px;
  transition: background 0.3s ease;
}

.submit-btn:hover {
  background-color: #4a8fa0;
}

.footer-note {
  text-align: center;
  font-size: 0.85rem;
  color: #a0aec0;
  margin-top: 20px;
  line-height: 1.4;
}

/* NEW: Keeps lower informational elements stacked and centered at 600px width */
.info-card-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 600px;
  padding: 0 20px;
  box-sizing: border-box;
}

.info-card {
  width: 100%;
  background: #ffffff;
  padding: 32px 40px;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
  margin-top: 4px;
  box-sizing: border-box;
}

.info-card h3 {
  font-family: "DM Sans", sans-serif;
  font-size: 1.25rem;
  font-weight: 700;
  color: #1a202c;
  margin-top: 0;
  margin-bottom: 24px;
}

.expect-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.expect-list li {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}

.expect-list p {
  font-family: "DM Sans", sans-serif;
  font-size: 1.05rem;
  line-height: 1.5;
  color: #4a5568;
  margin: 0;
}

.checkmark {
  color: #5ba4b5;
  font-weight: bold;
  font-size: 1.2rem;
  line-height: 1.2;
  user-select: none;
}

.urgent-notice-box {
  width: 100%;
  background-color: #eef5f7;
  border: 1px solid #d4e7eb;
  border-radius: 16px;
  padding: 24px 32px;
  margin-top: 24px;
  box-sizing: border-box;
}

.urgent-notice-box p {
  font-family: "DM Sans", sans-serif;
  font-size: 0.95rem;
  line-height: 1.6;
  color: #4a5568;
  margin: 0;
}

.urgent-notice-box strong {
  color: #1a202c;
  font-weight: 700;
}

.site-footer {
  width: 100%;
  background-color: #f8fafc; /* Matches your background wrapper color */
  border-top: 1px solid #e2e8f0;
  padding: 40px 0 30px 0;
  margin-top: 60px; /* Separates the page cards from the footer bottom area */
  font-family: "DM Sans", sans-serif;
  box-sizing: border-box;
}

.footer-container {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
  box-sizing: border-box;
  flex-wrap: wrap;
  gap: 20px;
}

/* Left Group */
.footer-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #2d3748;
  font-size: 1.15rem;
}

.copyright {
  font-size: 0.9rem;
  color: #718096;
}

/* Center Group Links */
.footer-center {
  display: flex;
  gap: 24px;
}

.footer-center a {
  text-decoration: none;
  font-size: 0.95rem;
  color: #4a5568;
  transition: color 0.2s ease;
}

.footer-center a:hover {
  color: #5ba4b5;
}

/* Right Group Social Icons */
.footer-right {
  display: flex;
  gap: 16px;
  align-items: center;
}

.social-icon {
  color: #a0aec0;
  transition: color 0.2s ease;
}

.social-icon:hover {
  color: #718096;
}

/* Medical Advice Disclaimer Bar */
.footer-disclaimer {
  max-width: 1100px;
  margin: 24px auto 0 auto;
  padding: 0 40px;
  box-sizing: border-box;
  text-align: left;
}

.footer-disclaimer p {
  font-size: 0.85rem;
  color: #a0aec0;
  line-height: 1.5;
  margin: 0;
}

/* ==========================================================================
   NEW RESPONSIIVE MOBILE MEDIA QUERIES (768px BREAKPOINT)
   ========================================================================== */
@media (max-width: 768px) {
  /* Navigation Bar Adjustments */
  .navBar {
    padding: 12px 16px;
    justify-content: space-between;
    position: relative;
  }
  .navBar img {
    width: 35%;
  }
  .links {
    display: none; /* Hides internal standard text links on small screens */
  }
  .logoText {
    width: auto;
  }

  /* Hero Typography Layout */
  .before,
  .during,
  .after {
    font-size: 16vw;
    width: 90%;
    text-align: center;
  }
  .hero p {
    width: 85%;
    font-size: 1.05rem;
  }
  .heroBtn {
    flex-direction: column;
    width: 85%;
    gap: 0.75rem;
  }
  .heroDarkBtn,
  .heroLightBtn {
    width: 100%;
    justify-content: center;
  }

  /* Core Journey Containers */
  .journey h2 {
    font-size: 2.2rem;
    text-align: center;
    padding: 0 16px;
  }
  .journeyDesc {
    width: 85%;
    font-size: 1rem;
  }

  /* Image & Text Flex Cards (Stacks layout vertically) */
  .cardOne,
  .cardTwo {
    flex-direction: column !important;
    gap: 32px;
    padding: 40px 16px;
  }
  .cardOneImageWrapper,
  .cardTwoImageWrapper,
  .cardThreeImageWrapper,
  .cardFourImageWrapper {
    width: 90% !important;
    margin: 0 auto;
  }
  .cardOneText,
  .cardTwoText {
    width: 90% !important;
    align-items: center;
    text-align: center !important;
  }
  .cardOneText h3,
  .cardTwoText h3,
  .questionOne,
  .questionTwo,
  .descOne,
  .descTwo {
    text-align: center !important;
  }
  .warn,
  .warnTwo {
    width: 100%;
    box-sizing: border-box;
    padding: 16px;
  }
  .cardFourImageWrapper img {
    width: 100%;
  }

  /* Medical Dashboard Counter Section */
  .medicalContainer {
    flex-direction: column;
    padding: 40px 16px;
  }
  .left,
  .right {
    width: 90% !important;
    align-items: center;
    text-align: center;
    margin: 0 auto;
  }
  .leftTitleOne,
  .leftTitleTwo {
    font-size: 2.2rem;
    width: 100%;
    margin-top: 12px;
  }
  .right {
    margin-top: 24px;
  }
  .right p {
    width: 100%;
    font-size: 1rem;
  }

  /* Grid Metric Cards Setup (2 columns wide instead of 4) */
  .fourCardsContainer {
    display: grid;
    grid-template-columns: 1fr 1fr;
    width: 90%;
    margin: 32px auto;
    gap: 16px;
  }
  .surgery,
  .average,
  .satisfaction,
  .education {
    width: 100%;
    margin-bottom: 0;
    box-sizing: border-box;
    align-items: center;
    text-align: center;
    height: 100%;
  }
  .fourCardCredits {
    flex-direction: column;
    gap: 10px;
    width: 90%;
    margin: 0 auto 40px auto;
  }
  .credits {
    margin-left: 0;
    text-align: center;
  }

  /* Review/Testimonial Box */
  .reviewContainer {
    margin-bottom: 64px;
  }
  .review {
    width: 85%;
    padding: 1.5rem;
  }
  .reviewDesc {
    font-size: 1.2rem;
    line-height: 1.5;
  }

  /* Accordion Layout Components (FAQ Split) */
  .questions {
    flex-direction: column;
    padding: 64px 16px;
    gap: 40px;
  }
  .questionsleft {
    margin-right: 0;
    align-items: center;
    text-align: center;
    width: 90%;
  }
  .questionsleft h2,
  .questionleftDesc {
    width: 100%;
  }
  .questionBtn {
    width: 100%;
  }
  .questionRight {
    width: 100%;
    margin: 0;
  }
  .faq-header {
    padding: 16px;
    gap: 12px;
  }
  .faq-left-meta {
    width: auto;
  }
  .faq-tag {
    margin-right: 0;
  }
  .faq-question {
    font-size: 1rem;
    margin-left: 0;
  }
  .faq-content p {
    padding: 0 16px 20px 16px; /* Breaks left indentation to fit narrow screens */
  }

  /* Booking Form and Information Area */
  .bookTitle h2 {
    font-size: 2rem;
  }
  .form-wrapper {
    flex-direction: column;
    align-items: center;
    gap: 32px;
    padding: 16px;
  }
  .form-card {
    padding: 24px 16px;
  }
  .form-grid-row {
    grid-template-columns: 1fr; /* Form inputs collapse into single stacks */
    gap: 0;
  }

  /* Footer Layout Grid Elements */
  .footer-container {
    flex-direction: column;
    text-align: center;
    padding: 0 20px;
  }
  .footer-left,
  .footer-center,
  .footer-right {
    justify-content: center;
    width: 100%;
  }
  .footer-center {
    gap: 16px;
  }
  .footer-disclaimer {
    padding: 0 20px;
    text-align: center;
  }
}
</style>
