// JQuery
var sidebar = 0;
var sidebarwd = "0%";
$(".menu-toggle").click(function(){
    if(sidebar == 0){ sidebar = 1; sidebarwd = "100%"; }else{ sidebar = 0; sidebarwd = "0%"; }
    $(".sidebar2").animate({opacity: 0.95,width: sidebarwd}, 300, function() {});
});

$(document).keyup(function(e) {
    if (e.key === "Escape") { // escape key maps to keycode `27`
        sidebar = 0; sidebarwd = "0%"; 
        if(sidebar == 0) $(".sidebar2").animate({opacity: 0.95,width: sidebarwd}, 300, function() {});
    }
    
});


