$(document).ready(function() {
    $('.select-country').select2({});
    $('.select-city').select2({
        language: "pt-BR",
        ajax: {
            url: window.location.origin + "/api/v1/cities/",
            delay: 250,
            data: function (params) {
                return {
                    country: $('#country').val(),
                    name: params.term
                };
            },
            processResults: function (data, params) {
                let items = [];
                $.each(data.results, function (index, value) {
                    items.push({
                        'id': value['code'],
                        'text': value['name']
                    })
                });
                return {
                    results: items,
                };
            },
        }
    });
    $('#buscar').click(function () {
        let code_city = $('#city').val();
        $.ajax({
          url: window.location.origin + `/api/v1/weather/${code_city}`,
          method: 'get',
          success: function (data, text) {
              $('.content-body').html(data)
          },
          error: function (request, status, error) {
              $('.content-body').html("<span style='color:red;'>"+request.responseJSON['detail']+"</span>")
          }
      });

    })
});
