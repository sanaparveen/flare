/**
 * Created by sana parveen on 17-07-2016.
 */

$(function(){
    var ws_scheme = window.location.protocol == "https:"?"wss":"ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme+ '://' + window.local.host + "/chat"+ window.location.pathname);

    chatsock.onmessage = function(message) {

        var data = JSON.parse(message.data);
        var chat = $("#chat")
        var ele = $('<tr></tr>')

                  ele.append(
                          $("<td></td>").text(data.timestamp)
                  );
                  ele.append(
                          $("<td></td>").text(data.creator)
                  );
                  ele.append(
                          $("<td></td>").text(data.text_message)
                  );
                  console.log("from chat");
                  chat.append(ele);
    };
    $("#chatform").on("submit", function(event) {

                  var message = {

                      creator: '{{ user.get_username }}',
                      text_message : $('#message').val()
                  };
                  chatsock.send(JSON.stringify(message));
                  $("#message").val('').focus();
                  console.log("from message");
                  return false;
    });

});