// main.js - Funcionalidades principales del sistema

document.addEventListener('DOMContentLoaded', function() {
    inicializarSistema();
    configurarEventos();
    inicializarGraficos();
    configurarNavegacion();
});

function inicializarSistema() {
    console.log('Sistema GESINFRA-WEB inicializado');
    
    // Configurar tema
    const temaGuardado = localStorage.getItem('tema') || 'claro';
    aplicarTema(temaGuardado);
    
    // Configurar sidebar en móviles
    configurarSidebarMovil();
    
    // Inicializar tooltips
    const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltips.forEach(element => {
        new bootstrap.Tooltip(element);
    });
    
    // Inicializar popovers
    const popovers = document.querySelectorAll('[data-bs-toggle="popover"]');
    popovers.forEach(element => {
        new bootstrap.Popover(element);
    });
}

function configurarEventos() {
    // Eventos del sidebar
    document.querySelectorAll('.sidebar .nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            if (window.innerWidth <= 768) {
                const sidebar = document.querySelector('.sidebar');
                if (sidebar) sidebar.classList.remove('show');
            }
        });
    });
    
    // Eventos de formularios
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = this.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.classList.add('is-invalid');
                    isValid = false;
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                mostrarAlerta('Por favor complete todos los campos requeridos.', 'danger');
            }
        });
    });
    
    // Eventos de confirmación
    document.querySelectorAll('[data-confirm]').forEach(element => {
        element.addEventListener('click', function(e) {
            const message = this.getAttribute('data-confirm') || '¿Está seguro de realizar esta acción?';
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    });
    
    // Eventos para modales de módulos
    document.querySelectorAll('[data-module]').forEach(element => {
        element.addEventListener('click', function(e) {
            e.preventDefault();
            const moduleId = this.getAttribute('data-module');
            mostrarModulo(moduleId);
        });
    });
    
    // Eventos para cerrar módulos
    document.querySelectorAll('.close-module').forEach(button => {
        button.addEventListener('click', function() {
            const moduleWindow = this.closest('.module-window');
            moduleWindow.style.display = 'none';
        });
    });
    
    // Evento para logout
    document.querySelectorAll('[href*="logout"]').forEach(link => {
        link.addEventListener('click', function(e) {
            if (!confirm('¿Está seguro de que desea cerrar sesión?')) {
                e.preventDefault();
            }
        });
    });
}

function configurarNavegacion() {
    // Eventos para enlaces de navegación
    document.querySelectorAll('[data-section]').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const sectionId = this.getAttribute('data-section');
            mostrarSeccion(sectionId);
            
            // Actualizar navegación activa en sidebar
            const sidebarLinks = document.querySelectorAll('.sidebar .nav-link');
            sidebarLinks.forEach(sidebarLink => {
                sidebarLink.classList.remove('active');
            });
            
            // Marcar como activo el enlace correspondiente
            const activeSidebarLink = document.querySelector(`.sidebar .nav-link[data-section="${sectionId}"]`);
            if (activeSidebarLink) {
                activeSidebarLink.classList.add('active');
            }
        });
    });
    
    // Mostrar dashboard al cargar si el usuario está autenticado
    const isAuthenticated = document.body.classList.contains('user-authenticated') || 
                           document.querySelector('[data-user-authenticated]');
    
    if (isAuthenticated && window.location.pathname === '/') {
        mostrarSeccion('dashboard');
    }
}

function mostrarSeccion(sectionId) {
    // Ocultar todas las secciones
    const sections = document.querySelectorAll('.dashboard-section, #welcome');
    sections.forEach(section => {
        section.classList.remove('active-section');
    });
    
    // Mostrar la sección solicitada
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.classList.add('active-section');
    }
}

function mostrarModulo(moduleId) {
    // Ocultar todos los módulos
    const modules = document.querySelectorAll('.module-window');
    modules.forEach(module => {
        module.style.display = 'none';
    });
    
    // Mostrar el módulo solicitado
    const targetModule = document.getElementById(`${moduleId}-module`);
    if (targetModule) {
        targetModule.style.display = 'block';
    }
}

function aplicarTema(tema) {
    if (tema === 'oscuro') {
        document.body.classList.add('tema-oscuro');
        document.body.classList.remove('tema-claro');
    } else {
        document.body.classList.add('tema-claro');
        document.body.classList.remove('tema-oscuro');
    }
    localStorage.setItem('tema', tema);
}

function configurarSidebarMovil() {
    const sidebarToggle = document.querySelector('[data-bs-target=".sidebar"]');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            document.querySelector('.sidebar').classList.toggle('show');
        });
    }
    
    // Cerrar sidebar al hacer clic fuera en móviles
    document.addEventListener('click', function(e) {
        if (window.innerWidth <= 768) {
            const sidebar = document.querySelector('.sidebar');
            const target = e.target;
            
            if (sidebar && sidebar.classList.contains('show') && 
                !sidebar.contains(target) && 
                !target.closest('[data-bs-target=".sidebar"]')) {
                sidebar.classList.remove('show');
            }
        }
    });
}

function mostrarAlerta(mensaje, tipo = 'info') {
    // Crear alerta
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${tipo} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        <i class="bi bi-${tipo === 'success' ? 'check-circle' : 'exclamation-triangle'} me-2"></i>
        ${mensaje}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Buscar contenedor de mensajes
    let container = document.querySelector('.messages');
    if (!container) {
        container = document.createElement('div');
        container.className = 'messages mb-3';
        const main = document.querySelector('main');
        if (main) {
            main.prepend(container);
        }
    }
    
    container.appendChild(alertDiv);
    
    // Auto-ocultar después de 5 segundos
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.style.opacity = '0';
            setTimeout(() => {
                if (alertDiv.parentNode) {
                    alertDiv.parentNode.removeChild(alertDiv);
                }
            }, 300);
        }
    }, 5000);
}

function inicializarGraficos() {
    // Inicializar gráficos si existen en la página
    if (document.getElementById('calificacionesChart')) {
        inicializarGraficoCalificaciones();
    }
    
    if (document.getElementById('equiposChart')) {
        inicializarGraficoEquipos();
    }
}

function inicializarGraficoCalificaciones() {
    const ctx = document.getElementById('calificacionesChart').getContext('2d');
    window.calificacionesChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['0-5', '5-6', '6-7', '7-8', '8-9', '9-10'],
            datasets: [{
                label: 'Número de Estudiantes',
                data: [2, 5, 8, 12, 15, 10],
                backgroundColor: [
                    'rgba(231, 76, 60, 0.7)',
                    'rgba(243, 156, 18, 0.7)',
                    'rgba(241, 196, 15, 0.7)',
                    'rgba(46, 204, 113, 0.7)',
                    'rgba(52, 152, 219, 0.7)',
                    'rgba(155, 89, 182, 0.7)'
                ],
                borderColor: [
                    'rgba(231, 76, 60, 1)',
                    'rgba(243, 156, 18, 1)',
                    'rgba(241, 196, 15, 1)',
                    'rgba(46, 204, 113, 1)',
                    'rgba(52, 152, 219, 1)',
                    'rgba(155, 89, 182, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function inicializarGraficoEquipos() {
    const ctx = document.getElementById('equiposChart').getContext('2d');
    window.equiposChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Activos', 'Mantenimiento', 'Baja'],
            datasets: [{
                data: [75, 15, 10],
                backgroundColor: [
                    'rgba(46, 204, 113, 0.7)',
                    'rgba(241, 196, 15, 0.7)',
                    'rgba(231, 76, 60, 0.7)'
                ],
                borderColor: [
                    'rgba(46, 204, 113, 1)',
                    'rgba(241, 196, 15, 1)',
                    'rgba(231, 76, 60, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

// Funciones utilitarias globales
window.mostrarAlerta = mostrarAlerta;
window.mostrarSeccion = mostrarSeccion;
window.mostrarModulo = mostrarModulo;

// Formato de fecha
function formatDate(date) {
    return new Date(date).toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

// Formato de número
function formatNumber(number) {
    return new Intl.NumberFormat('es-ES').format(number);
}

// Confirmación de acciones
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}
