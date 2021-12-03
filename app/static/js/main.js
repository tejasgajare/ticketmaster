$(document).ready(function() {
    setPagination();
    setTicketLinks();
    setStatusClasses();
    setDates();
    console.log("ready " + moment().startOf('day').fromNow());
});

function setDates(){
    $(".updated").each(function(){
        let updated = $(this).text();
        $(this).text(moment(updated, "YYYY-MM-DD HH:mm Z").format('ll'));
    });
}

function setStatusClasses(){
    
    $('.status').each(function(){
        let status = $(this).text();
        console.log(status);
        if (status == "New"){
            $(this).addClass("bg-warning");
            $(this).addClass("text-dark");
        } else if (status == "open"){
            $(this).addClass("bg-danger");
        } else if (status == "pending"){
            $(this).addClass("bg-info");
            $(this).addClass("text-dark");
        } else if (status == "on-hold"){
            $(this).addClass("bg-dark");
        }  else if (status == "solved"){
            $(this).addClass("bg-secondary");
        }
    });
}

function setPagination(){
    $(".pagination>.page-item>.page-link").each(function() {
        if ($(this).attr("pagelink") == "None") {
            $(this).parent().addClass("disabled");
        } else {
            let page = getParameterByName("page", $(this).attr("pagelink"));
            $(this).attr("href", "?page=" + page);
        }
    });
}

function setTicketLinks(){
    $('tr[data-href]').on("click", function() {
        document.location = $(this).data('href');
    });
}

function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}