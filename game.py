import streamlit as st
import pymongo

# 连接MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ip_db"]
collection = db["ip_addresses"]

# 页面标题和文本框
st.title("IP地址审核")
ip_address_a = st.text_input("请输入IP地址 A：")
ip_address_b = st.text_input("请输入IP地址 B：")

# 提交按钮
if st.button("提交"):
    # 查询是否存在相同的记录
    existing_record = collection.find_one({"ip_address_a": ip_address_a})
    if existing_record:
        # 如果存在相同记录，检查IP地址B是否相同
        if existing_record["ip_address_b"] == ip_address_b:
            st.warning("已有相同记录，可以通过")
        else:
            st.warning("已有不同的用户使用该IP，请驳回！")
    else:
        # 如果不存在相同记录，则插入新记录
        new_record = {"ip_address_a": ip_address_a, "ip_address_b": ip_address_b}
        collection.insert_one(new_record)
        st.success("该IP为首次使用，请放心审核。")
