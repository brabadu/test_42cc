$(document).ready(function() { 
    // bind form using ajaxForm 
    $('#contact_form').ajaxForm({ 
        target: '#output_result', 
        url: '/ajax_contacts_edit/',

        success: function() { 
//            $('#output_result').fadeIn('slow'); 
        } 
    }); 
});
