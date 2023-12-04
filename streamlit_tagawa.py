
import streamlit as st 
from streamlit_folium import folium_static



st.title('善光寺観光にぴったり！おすすめのお店たち！')
st.write('善光寺周辺にはたくさんのお店があります。どこのお店が美味しいのかな？、人気が高いのかな？、今の気分に合っているのかな？、など迷うことも多々あるでしょう。そんなあなたに、今の状況や気分にぴったりなお店を提案しちゃいます！')

condition = st.slider('お腹どれくらい空いてますか？(100がお腹いっぱい,0が腹ぺこ)',0,100,50)
text = st.text_input('今の気分はどうですか？')
st.write('今のあなたの気分は、'+text+'なのですね！')

import time
st.sidebar.write('プログレスバーの表示')
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'わくわく！どきどき！準備中...{i+1}')
  bar.progress(i+1)
  time.sleep(0.1)


import folium
from streamlit_folium import folium_static
import streamlit as st
import pandas as pd
import streamlit_folium



import streamlit as st
from streamlit_folium import folium_static
import folium

def main():
    st.title("★おすすめのお店★")

    # 選択オプションのリスト
    location_options = ['がっつり本格的に食べることができるお店','ランチに行きたい！こ洒落たお店','小腹を充たせる程度の食べ歩きで楽しみたいお店','デザートや甘い物などを楽しむことができるお店','お腹は空いていないので散策したい']
    
    # オプションの選択
    selected_location = st.selectbox('今の気分とお腹の空き具合に合った、探したいお店を選択します。', location_options)

    # オプションに対応する座標
    coordinates = {
        'がっつり本格的に食べることができるお店': (36.66437, 138.18808),
        'ランチに行きたい！こ洒落たお店': (36.65759, 138.18785),
        '小腹を満たせる程度の食べ歩きで楽しみたいお店': (36.65883, 138.18765),
        'デザートや甘い物などを楽しむことができるお店': (36.65987, 138.18770),
        'お腹は空いていないので散策したい': (36.66539, 138.19358),
    }

    # 選択された場所に対応する座標を取得
    selected_coordinates = coordinates.get(selected_location)

    if selected_coordinates:
        st.write(f"あなたが選んだのは {selected_location}")

        
        # Foliumを使用して地図を作成
        m = folium.Map(location=selected_coordinates, zoom_start=17)
        
        # マーカーを追加
        folium.Marker(location=selected_coordinates, popup=selected_location).add_to(m)
        

        # Foliumの地図をStreamlitに表示
        folium_static(m)
    else:
        st.warning("Please select a valid location.")

if __name__ == "__main__":
    main()

import streamlit as st

def main():
    st.write("お店について詳しく！")

    # オプションとそれに対する説明の辞書
    options_with_description = {
        'がっつり本格的に食べることができるお店：とんかつ健': 'とんかつ健について: 大きくて分厚い、粗めのパン粉でサクサクとした上がり具合のかつが美味しい。とんかつと盛りの良さが評判。お店の雰囲気としてはとてもアットホームで、居心地がよい。',
        'ランチに行きたい！こ洒落たお店: 横町カフェ': '横町カフェについて: 「七味で有名な八幡屋磯五郎のShopに併設している。沢山の種類の七味が各テーブルに置かれていて、自由に使うことができる。自社農場産や信州産の新鮮な素材を多く使用していて、信州の良さ魅力がよく伝わる。',
        '小腹を満たせる程度の食べ歩きで楽しみたいお店: つち茂物産店': 'つち茂物産店について: 店先で、焼きたてのおやきを食べることができる。アツアツでとても美味しい。おすすめは、他の店ではあまり見かけることのない、ねぎ味噌チーズとラー油野沢菜である。',
        'デザートや甘い物などを楽しむことができるお店: 抹茶館-善光寺仲見世通り店': '抹茶館について: 京都の老舗『森半』の上質な茶葉を使用したスイーツとお茶のメニューたちを楽しむことができる。甘さよりも抹茶本来の風味を味わうことができる。',
        'お腹は空いていないので散策したい: 城山動物園 ': '城山動物園について: アシカをはじめとした、さまざまな動物がいる。入園無料で、にぎやかで楽しい。遊具もあって楽しく、子連れの家族が多い。',
    }

    # オプションの選択
    selected_option = st.selectbox('詳しく知りたいお店を選択します。', list(options_with_description.keys()))

    # 選んだオプションに対する説明を表示
    st.markdown(options_with_description[selected_option])

if __name__ == "__main__":
    main()

