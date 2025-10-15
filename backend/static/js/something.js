// DOM Elements
const navLinks = document.querySelectorAll('.nav-link');
const sections = document.querySelectorAll('main > section');
const loginBtn = document.getElementById('loginBtn');
const signupBtn = document.getElementById('signupBtn');
const heroLoginBtn = document.getElementById('heroLoginBtn');
const heroCheckinBtn = document.getElementById('heroCheckinBtn');
const formTitle = document.getElementById('formTitle');
const authForm = document.getElementById('authForm');
const nameGroup = document.getElementById('nameGroup');
const confirmPasswordGroup = document.getElementById('confirmPasswordGroup');
const formFooterText = document.getElementById('formFooterText');
const toggleForm = document.getElementById('toggleForm');
const checkinForm = document.getElementById('checkinForm');
const chatbotToggle = document.getElementById('chatbotToggle');
const chatbotWindow = document.getElementById('chatbotWindow');
const chatbotClose = document.getElementById('chatbotClose');
const chatbotMessages = document.getElementById('chatbotMessages');
const chatbotInput = document.getElementById('chatbotInput');
const chatbotSend = document.getElementById('chatbotSend');
const themeToggle = document.getElementById('themeToggle');
// Chatbot functionality


// Chatbot state
let isChatbotLoading = false;

chatbotToggle.addEventListener('click', function() {
    chatbotWindow.classList.toggle('active');
});

chatbotClose.addEventListener('click', function() {
    chatbotWindow.classList.remove('active');
});

function addMessage(message, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = isUser ? 'message user-message' : 'message bot-message';
    messageDiv.textContent = message;
    chatbotMessages.appendChild(messageDiv);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

function addLoadingIndicator() {
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'message bot-message loading-indicator';
    loadingDiv.id = 'loadingIndicator';
    loadingDiv.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Thinking...';
    chatbotMessages.appendChild(loadingDiv);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

function removeLoadingIndicator() {
    const loadingIndicator = document.getElementById('loadingIndicator');
    if (loadingIndicator) {
        loadingIndicator.remove();
    }
}

async function sendMessageToAPI(message) {
    try {
        const csrfToken = getCSRFToken();
        
        const response = await fetch('/chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
                message: message,
                system_prompt: `You are HealthSync AI, a helpful and empathetic healthcare assistant. When users mention symptoms like fever, respond helpfully with:

1. Ask relevant follow-up questions (duration, temperature, other symptoms)
2. Provide general self-care advice (rest, hydration, fever management)
3. Suggest when to see a doctor based on symptom severity
4. Always include a brief disclaimer about consulting healthcare professionals

Be specific and helpful. For example, if someone says "I have fever", respond with:
- "I'm sorry to hear you're not feeling well. How long have you had the fever? Have you taken your temperature? Any other symptoms like cough or body aches?"
- Then provide general care tips and guidance on when to seek medical attention.

Provide practical, helpful information while being clear you're an AI assistant.`,
                model: 'gpt-3.5-turbo',
                max_tokens: 500
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        return data.message;
        
    } catch (error) {
        console.error('Error calling chat API:', error);
        return "I'm sorry, I'm having trouble connecting right now. Please try again later.";
    }
}
function getCSRFToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfToken ? csrfToken.value : '';
}

chatbotSend.addEventListener('click', async function() {
    await handleChatbotSend();
});

chatbotInput.addEventListener('keypress', async function(e) {
    if (e.key === 'Enter') {
        await handleChatbotSend();
    }
});

async function handleChatbotSend() {
    const message = chatbotInput.value.trim();
    
    if (message && !isChatbotLoading) {
        // Add user message
        addMessage(message, true);
        chatbotInput.value = '';
        
        // Show loading indicator
        addLoadingIndicator();
        isChatbotLoading = true;
        chatbotSend.disabled = true;
        
        try {
            // Get AI response
            const aiResponse = await sendMessageToAPI(message);
            
            // Remove loading indicator and add AI response
            removeLoadingIndicator();
            addMessage(aiResponse, false);
            
        } catch (error) {
            removeLoadingIndicator();
            addMessage("Sorry, I encountered an error. Please try again.", false);
        } finally {
            isChatbotLoading = false;
            chatbotSend.disabled = false;
        }
    }
}

// Auto-focus on input when chatbot opens
chatbotToggle.addEventListener('click', function() {
    setTimeout(() => {
        if (chatbotWindow.classList.contains('active')) {
            chatbotInput.focus();
        }
    }, 300);
});
// Auth Form Toggle

const submitBtn = document.getElementById('submitBtn');
const formType = document.getElementById('formType');
const hiddenEmail = document.getElementById('hiddenEmail');
const emailInput = document.getElementById('email');

let isLoginForm = true;

// Sync email field with hidden email field
emailInput.addEventListener('input', function() {
    hiddenEmail.value = this.value;
});

toggleForm.addEventListener('click', function(e) {
    e.preventDefault();
    isLoginForm = !isLoginForm;
    
    if (isLoginForm) {
        // Switch to Login form
        formTitle.textContent = 'Login to HealthSync';
        nameGroup.style.display = 'none';
        confirmPasswordGroup.style.display = 'none';
        formFooterText.innerHTML = 'Don\'t have an account? <a href="#" id="toggleForm">Sign Up</a>';
        submitBtn.textContent = 'Login';
        formType.value = 'login';
        
        // Remove required from signup-only fields
        document.getElementById('name').removeAttribute('required');
        document.getElementById('confirmPassword').removeAttribute('required');
    } else {
        // Switch to Signup form
        formTitle.textContent = 'Sign Up for HealthSync';
        nameGroup.style.display = 'block';
        confirmPasswordGroup.style.display = 'block';
        formFooterText.innerHTML = 'Already have an account? <a href="#" id="toggleForm">Login</a>';
        submitBtn.textContent = 'Sign Up';
        formType.value = 'signup';
        
        // Add required to signup fields
        document.getElementById('name').setAttribute('required', 'required');
        document.getElementById('confirmPassword').setAttribute('required', 'required');
    }
    
    // Re-attach event listener
    document.getElementById('toggleForm').addEventListener('click', arguments.callee);
});

// Form submission
authForm.addEventListener('submit', function(e) {
    if (!isLoginForm) {
        // Signup validation
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        
        if (password !== confirmPassword) {
            e.preventDefault();
            alert('Passwords do not match!');
            return false;
        }
    }
    
    // Set the form action based on form type
    if (isLoginForm) {
        this.action = "{% url 'signin' %}";
    } else {
        this.action = "{% url 'signup' %}";
    }
    
    return true;
});

// Theme Management
function initTheme() {
    const savedTheme = localStorage.getItem('healthsync-theme') || 'light-mode';
    document.body.className = savedTheme;
    themeToggle.checked = savedTheme === 'dark-mode';
}

function toggleTheme() {
    if (themeToggle.checked) {
        document.body.classList.remove('light-mode');
        document.body.classList.add('dark-mode');
        localStorage.setItem('healthsync-theme', 'dark-mode');
    } else {
        document.body.classList.remove('dark-mode');
        document.body.classList.add('light-mode');
        localStorage.setItem('healthsync-theme', 'light-mode');
    }
}

// Navigation
function showSection(sectionId) {
    sections.forEach(section => {
        section.classList.add('hidden');
        section.classList.remove('active-section');
    });
    
    document.getElementById(sectionId).classList.remove('hidden');
    document.getElementById(sectionId).classList.add('active-section');
    
    // Trigger animations for elements in the active section
    setTimeout(() => {
        const fadeElements = document.querySelectorAll(`#${sectionId} .fade-in`);
        fadeElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
        });
        
        setTimeout(() => {
            fadeElements.forEach(el => {
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            });
        }, 100);
    }, 50);
}

// Event Listeners for Navigation
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const sectionId = link.getAttribute('data-section');
        showSection(sectionId);
    });
});

loginBtn.addEventListener('click', () => {
    showSection('login');
    setLoginMode();
});

signupBtn.addEventListener('click', () => {
    showSection('login');
    setSignupMode();
});

heroLoginBtn.addEventListener('click', () => {
    showSection('login');
    setLoginMode();
});

heroCheckinBtn.addEventListener('click', () => {
    showSection('checkin');
});

// Auth Form Toggle
let isLoginMode = true;

function setLoginMode() {
    isLoginMode = true;
    formTitle.textContent = 'Login to HealthSync';
    nameGroup.style.display = 'none';
    confirmPasswordGroup.style.display = 'none';
    authForm.querySelector('button').textContent = 'Login';
    formFooterText.innerHTML = 'Don\'t have an account? <a href="#" id="toggleForm">Sign Up</a>';
    document.getElementById('toggleForm').addEventListener('click', toggleAuthMode);
}

function setSignupMode() {
    isLoginMode = false;
    formTitle.textContent = 'Create an Account';
    nameGroup.style.display = 'block';
    confirmPasswordGroup.style.display = 'block';
    authForm.querySelector('button').textContent = 'Sign Up';
    formFooterText.innerHTML = 'Already have an account? <a href="#" id="toggleForm">Login</a>';
    document.getElementById('toggleForm').addEventListener('click', toggleAuthMode);
}

function toggleAuthMode(e) {
    e.preventDefault();
    if (isLoginMode) {
        setSignupMode();
    } else {
        setLoginMode();
    }
}

// Form Submissions
authForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (isLoginMode) {
        alert('Login successful! Redirecting to dashboard...');
    } else {
        alert('Account created successfully! Please check your email for verification.');
    }
    showSection('home');
});

checkinForm.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Check-in submitted successfully! A healthcare professional will review your information shortly.');
    showSection('home');
});

// Chatbot Functionality
chatbotToggle.addEventListener('click', () => {
    chatbotWindow.style.display = 'flex';
});

chatbotClose.addEventListener('click', () => {
    chatbotWindow.style.display = 'none';
});

function addMessage(message, isUser) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.classList.add(isUser ? 'user-message' : 'bot-message');
    messageDiv.textContent = message;
    chatbotMessages.appendChild(messageDiv);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

function getBotResponse(message) {
    const responses = {
        'hello': 'Hello! How can I assist you with your health concerns today?',
        'hi': 'Hi there! I\'m HealthSync Assistant. How can I help you?',
        'symptoms': 'I can help you understand common symptoms. However, please remember I\'m not a substitute for professional medical advice. For serious symptoms, contact a healthcare provider immediately.',
        'appointment': 'To book an appointment with a healthcare professional, please visit our "Services" section or call our support line at +1 (555) 123-4567.',
        'medicine': 'I can provide general information about medications, but always consult with a pharmacist or doctor before taking any new medication.',
        'emergency': 'If this is a medical emergency, please call emergency services immediately. Do not rely on this chatbot for emergency situations.',
        'default': 'I\'m here to help with general health information. For specific medical advice, please consult with a healthcare professional. How else can I assist you?'
    };

    message = message.toLowerCase();
    
    for (const keyword in responses) {
        if (message.includes(keyword)) {
            return responses[keyword];
        }
    }
    
    return responses['default'];
}

chatbotSend.addEventListener('click', () => {
    const message = chatbotInput.value.trim();
    if (message) {
        addMessage(message, true);
        chatbotInput.value = '';
        
        // Simulate typing delay
        setTimeout(() => {
            const response = getBotResponse(message);
            addMessage(response, false);
        }, 1000);
    }
});

chatbotInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        chatbotSend.click();
    }
});

// Initialize
function init() {
    initTheme();
    setLoginMode();
    document.getElementById('toggleForm').addEventListener('click', toggleAuthMode);
    themeToggle.addEventListener('change', toggleTheme);

    // Animate feature cards on page load
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        card.style.animationDelay = `${0.1 + index * 0.2}s`;
    });
}

// Start the application
document.addEventListener('DOMContentLoaded', init);