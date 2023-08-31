
        $(document).ready(function () {

            $("#short-description").click(function () {
                $(".full-description").toggle();
            });


            function getCookie(c_name) {
                if (document.cookie.length > 0) {
                    c_start = document.cookie.indexOf(c_name + "=");
                    if (c_start !== -1) {
                        c_start = c_start + c_name.length + 1;
                        c_end = document.cookie.indexOf(";", c_start);
                        if (c_end === -1) c_end = document.cookie.length;
                        return (document.cookie.substring(c_start, c_end));
                    }
                }
                return "";
            }})

        //     $.ajaxSetup({
        //         headers: {"X-CSRFToken": getCookie("csrftoken")}
        //     });
        //     getElementById('myCheckbox').addEventListener("change", changeStatus);
        //
        // })


        function changeStatus(task_id, status) {


            let url = window.location.href
            let get_status = status !== true;
            let tbl = document.getElementById('todo-table')
            let elements = tbl.getElementsByTagName("input")
            let todo_row = document.getElementsByTagName("tr")
            let el_tr=document.getElementById("completed")

            if (document.getElementById("myCheckbox").checked === true) {
                el_tr.classList.toggle('completed')
            } else {
                  el_tr.classList.toggle('completed')

            }
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            $.ajax({
                type: 'POST',
                mode: 'same-origin',
                url: url,
                 headers:{
        "X-CSRFToken": csrftoken
    },
                data: {
                    task_id: task_id,
                    is_true: get_status
                },
                success: delayStatus ()

            })
            //
            function sleep(ms) {
                return new Promise(resolve => setTimeout(resolve, ms));
            }

            //это конечно тот еще костыль, но оно работает
            async function delayStatus() {
                await sleep(500);
                location.reload()
            }

            delayStatus();

        }

   function showFull(el) {

            let nextEl = document.getElementById(el)

            if (nextEl.style.display === 'table-cell' && nextEl.tagName === 'SPAN') {
                nextEl.style.display = 'none'

            } else if (nextEl.style.display === 'none' && nextEl.tagName === 'SPAN') {

                nextEl.style.display = 'table-cell'

            }
            return false
        }