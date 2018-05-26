let appState = {
    togglePulse: true,
    headerCollapsed: true,
}

let headerCollapse = function() {
    // Stop pulsating since the toggle has been acknowledged.
    appState.togglePulse = false;
    let headerToggle = document.getElementById("header-toggle-icon");
    headerToggle.setAttribute("pulse", appState.togglePulse);

    let header = document.getElementById("smallscreen-info-pane");
    header.setAttribute("show", appState.headerCollapsed);
    appState.headerCollapsed = !appState.headerCollapsed;
}

/**
 * Register events for the webpage.
 */
let registerEvents = function() {
    document.getElementById("header-toggle").addEventListener("click", headerCollapse);
}
