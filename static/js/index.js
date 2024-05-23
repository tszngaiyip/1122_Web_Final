const rest_name = '卡利西里'


$(document).ready(function(){
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
        event.preventDefault();
        let queryUrl = '/query?rn=' + rest_name;
        let foodType = $("input[name='food_type[]']:checked").val();
        queryUrl += `&ft=${encodeURIComponent(foodType)}`;
        queryUrl += '&rs='+Math.random();
        fetchData(queryUrl);
    });

    $("#submit-button").click(function (event) {

    });
});