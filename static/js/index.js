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
        $('#buscar').addClass('disabled-search');
        let code_city = $('#city').val();
        $('.content-body').html("");
        $.ajax({
          url: window.location.origin + `/api/v1/weather/${code_city}`,
          method: 'get',
          success: function (data, text) {
              $('.content-body').html(data)
              $('#buscar').removeClass('disabled-search');
          },
          error: function (request, status, error) {
              $('#buscar').removeClass('disabled-search');
              let text_error = request.statusText;
              if (request.status === 401){
                  text_error = "Não autorizado!";
              } else{
                  if (request.status === 400){
                      text_error = "Parâmetros inválidos!";
                  }
              }
              $('.content-body').html("<span style='color:red;'>"+text_error+"</span>")

          }
      });

    })
});
