$(document).ready( function() {    

    $(".url_button").on('click', function(en){
        
        $.ajax({
            url: "/links/read/bookmark/",
            type: "POST",
            async: false,
            data: {
                // name: value, // data you need to pass to your function
                 click: true, 
                 csrfmiddlewaretoken: getCookie('csrftoken'),
                 button_url: $(this).attr( "href" )
            }
         });
        // en.preventDefault();
    });

});

// https://docs.djangoproject.com/en/2.0/ref/csrf/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');