$.ajaxSetup({
    'beforeSend': function(request) {
        request.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'))
    }
});

$(document).ready(function() {
    $('a#follow').click(function(e) {
        let current_action = this.getAttribute('data-action');
        let person_id = $(this).data('id');
        e.preventDefault();
        $.ajax({
            method: 'POST',
            url: 'http://127.0.0.1:8000/accounts/follow/',
            data: {'user_id': person_id, 
                   'action': current_action}
        }).then(function(data) {
            if (data['status'] == 'ok') {
                let followers_counter = $(e.target).parent().find('.counter');
                if (current_action == 'follow') {
                    followers_counter.text(parseInt(followers_counter.text()) + 1);
                } else if (current_action == 'unfollow') {
                    followers_counter.text(parseInt(followers_counter.text()) - 1);
                }
                current_action = current_action == 'follow' ? 'unfollow' : 'follow';
                e.target.setAttribute('data-action', current_action);
                e.target.text = current_action.charAt(0).toUpperCase() + current_action.slice(1);
            }
        });
    });
});