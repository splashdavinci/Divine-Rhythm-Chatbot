import aio_pika.abc
import sqlite3
from typing import Any, Text, Dict, List
from rasa_sdk import Action
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
import tensorflow as tf
from connectdb import register_user, get_order_info_by_number
import http.server
    
class ActionRegisterUser(Action):
    def name(self) -> Text:
        return "action_register_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # 获取前端传递的参数
        user_id = tracker.get_slot("user_id")
        email = tracker.get_slot("email")

        register_user(user_id, email)
        dispatcher.utter_message("Registered successfully！")

        return []

class ActionGetOrderInfo(Action):
    def name(self) -> Text:
        return "action_get_order_info_by_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        order_number = tracker.get_slot("order_number")
        order_info = get_order_info_by_number(order_number)
        
        if order_info:
            dispatcher.utter_message(f"Order information：{order_info}")
        else:
            dispatcher.utter_message("The order cannot be found！")

        return []

# class ActionDefaultAskAffirmation(Action):
#     def name(self) -> Text:
#         return "action_default_ask_affirmation"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
#         # 从用户意图中获取澄清信息
#         user_intent = tracker.latest_message['intent'].get('name')
        
#         # 根据用户意图展示可能的答案和提供人工帮助的选项
#         response = f"您是指 {user_intent} 吗？请确认或提供更多细节。如果需要人工帮助，请告诉我。"
        
#         dispatcher.utter_message(text=response)
        
#         return []

# class ActionDefaultFallback(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
#         # 表达机器人的不确定性
#         response = "抱歉，我对您的问题感到困惑。我将寻求人工帮助以获得更准确的回答。"
        
#         # 告知用户将有人工帮助
#         response += "稍后会有人工客服与您联系。"
        
#         dispatcher.utter_message(text=response)
        
#         return []


# class StoreEmailContactAction(Action):
#     def name(self) -> Text:
#         return "store_email_contact"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         email = tracker.latest_message.get('entities')[0]['value']

#         # 调用 connectdb.py 中的函数更新待联系字段
#         update_contact_status(email)

#         dispatcher.utter_message("It has been marked as to be contacted, please wait patiently and we will contact you by email.")
#         return []
          
      