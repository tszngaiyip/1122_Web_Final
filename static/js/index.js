const rest_name = '卡利西里'

//chatbot animation
$(document).ready(function() {
    $('#chatbot-button').click(function() {
        $('#chatbot-dialog').toggleClass('show');
    });
});

// 顯示本月的公休時間
$(document).ready(function() {
    function generateRestDays() { // 生成本月的公休日期
        let restDays = [];
        let date = new Date();
        // let date = new Date(2024, 6, 1); //for testing
        let month = date.getMonth();
        let year = date.getFullYear();

        date.setDate(1);

        while (date.getDay() !== 1) {
            date.setDate(date.getDate() + 1);
        }

        while (date.getMonth() === month) {
            restDays.push(new Date(date.getTime()));
            date.setDate(date.getDate() + 7);
        }

        return restDays;
    }

    // 將公休日期添加到#left_di元素中
    let restDays = generateRestDays();
    let restDaysString = restDays.map(date => `${date.getMonth() + 1}/${date.getDate()}`).join(', ');

    $(".left_di").append("&nbsp<h4>"+restDaysString+"</h4>");
    });

$(document).ready(function(){
    $("#submit-button").prop('disabled', true);
    $("#submit-button").css('background-color', 'grey');

    // gray out the submit button
    $("#submit-button").prop('disabled', true);
    function fetchData(queryUrl) {
        fetch(queryUrl)
            .then(response => response.json())
            .then(data => {
                $("#result-food-type").text(data["food_type"]);
                $("#result-food-name").text(data["food_name"]);
                $("#result-food-price").text(data["food_price"]);
            })
            .catch(error => {
                $("#result-food-type").text("NULL");
                $("#result-food-name").text("查詢錯誤");
                $("#result-food-price").text("N/A");
            });
    }

    $("#filter-button").click(function(event){
        // enable the submit button
        $("#submit-button").prop('disabled', false);
        $("#submit-button").css('background-color', '#ffffff');

        event.preventDefault();
        let queryUrl = '/query?';
        let foodType = $("input[name='food_type[]']:checked").val();
        queryUrl += `ft=${encodeURIComponent(foodType)}`;
        queryUrl += '&rs='+Math.random();
        fetchData(queryUrl);
    });

    $("#submit-button").click(function (event) {
        // 修改按鈕文字和狀態
        $("#submit-button").text('請稍候');
        $("#submit-button").prop('disabled', true);
        $("#submit-button").css('background-color', 'grey');

        // 等待0.5到2秒後改變按鈕文字
        setTimeout(function () {
            $("#submit-button").text('已送出');

            // 再次等待一小段時間，確保文字更新
            setTimeout(function () {
                // 顯示彈出視窗
                window.alert('成功送出訂單');

                // 重定向到新頁面
                window.location.href = '/';
            }, 100); // 短暫等待100毫秒，確保按鈕文字更新
        }, Math.random() * 1500 + 500);
    });
});