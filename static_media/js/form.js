$(document).ready(function() { 
    // bind form using ajaxForm 
    $('#contact_form').ajaxForm({ 
        target: '#output_result', 
        url: '/ajax_contacts_edit/',
        beforeSubmit: function(formData, jqForm, options){
            $('input, textarea').attr('disabled', 'disabled');
            return true;
        },
        success: function() { 
            $("input, textarea").removeAttr("disabled");
        } 
    }); 
});
