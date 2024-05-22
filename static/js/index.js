$(document).ready(function(){
    function fetchData(queryUrl) {
        fetch(queryUrl)
            .then(response => response.json())
            .then(data => {
                // 处理并显示 JSON 数据
                let resultHtml = '';
                if (Array.isArray(data)) {
                    data.forEach(item => {
                        resultHtml += `<p>${JSON.stringify(item)}</p>`;
                    });
                } else {
                    resultHtml = `<p>${JSON.stringify(data)}</p>`;
                }
                document.getElementById("result").innerHTML = resultHtml;
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById("result").innerHTML = 'Error occurred while fetching data.';
            });
    }

    $("#filter-button").click(function(event){
        event.preventDefault();
        let foodType = $("input[name='food_type[]']:checked").val();
        let restaurantName = $("#select").val();
        let queryUrl = '/query?';
        let queryParams = [];

        if (restaurantName || foodType) {
            if (restaurantName) {
                queryParams.push(`rn=${encodeURIComponent(restaurantName)}`);
            }
            if (foodType) {
                queryParams.push(`mt=${encodeURIComponent(foodType)}`);
            }
            queryUrl += queryParams.join('&');
        }
        queryUrl += '&rs='+Math.random();
        fetchData(queryUrl);
    });

    $("#randomly_pick").click(function (event) {
        console.log('randomly_pick');
        event.preventDefault();

        let queryUrl = '/query?rs='+Math.random();
        fetchData(queryUrl);
    });
});