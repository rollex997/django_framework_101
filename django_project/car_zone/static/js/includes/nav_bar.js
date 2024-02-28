 function changeColor(element) {
        // Get all navbar items
        var navItems = document.getElementsByClassName('nav-link');

        // Loop through all navbar items
        for (var i = 0; i < navItems.length; i++) {
            // Reset the color of all navbar items to default (black)
            navItems[i].style.color = '';
        }

        // Set the color of the clicked navbar item to red
        element.style.color = 'red';
    }