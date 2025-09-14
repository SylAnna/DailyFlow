document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendar');
    

    const eventsData = JSON.parse(document.getElementById('calendar-data').textContent);

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',  // Default view (month grid)
        headerToolbar: {
            left: 'prev,next today',  // Left toolbar buttons
            center: 'title',          // Title in the center
            right: ''                 // No right toolbar buttons
        },
        events: eventsData,  // Pass events to FullCalendar
        eventColor: '#3B82F6',  // Blue color for events
        eventTextColor: 'white',  // White text for events
        eventDidMount: function(info) {
            // Tooltip on hover
            info.el.title = `${info.event.title}\nCategory: ${info.event.extendedProps.category}`;
        },
        eventClick: function(info) {
            // Display task info when clicked
            alert(`Task: ${info.event.title}\nCategory: ${info.event.extendedProps.category}`);
        },
        eventDidMount: function(info) {
            info.el.style.fontFamily = 'Arial, sans-serif';
            info.el.style.fontSize = '10px';
            info.el.title = `${info.event.title}\nCategory: ${info.event.extendedProps.category}`;
        }
    });

    calendar.render();
});
