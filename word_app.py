import streamlit as st
import random

# 整合 Unit 9 & Unit 10 所有核心單字、詞性、中文意思與英文定義
WORD_BANK = {
    "Unit 9: High-Tech Solutions": {
        "actual": {"pos": "adj.", "zh": "現實存在的；實際的", "def": "presently existing in fact"},
        "alter": {"pos": "v.", "zh": "改變；修改", "def": "to change something slightly"},
        "conference": {"pos": "n.", "zh": "會議；正式研討會", "def": "a prearranged meeting"},
        "conversely": {"pos": "adv.", "zh": "相反地", "def": "with the relation reversed"},
        "demonstrate": {"pos": "v.", "zh": "證明；示範；展現", "def": "to give an exhibition of to an interested audience"},
        "downside": {"pos": "n.", "zh": "缺點；負面面向", "def": "a negative aspect of something"},
        "get to": {"pos": "v.", "zh": "開始；著手；到達", "def": "to arrive at the point of"},
        "go over": {"pos": "v.", "zh": "仔細檢查；複習", "def": "to examine so as to determine accuracy, quality, or condition"},
        "passive": {"pos": "adj.", "zh": "被動的", "def": "allowing other people to be in control"},
        "treat": {"pos": "v.", "zh": "治療；對待", "def": "to behave towards someone or something in a particular way"},
        "affordable": {"pos": "adj.", "zh": "負擔得起的；價格合理的", "def": "cheap enough for most people to afford"},
        "aid": {"pos": "n.", "zh": "援助；幫助", "def": "help, such as money or food"},
        "ambitious": {"pos": "adj.", "zh": "有野心的；宏大的", "def": "determined to be successful, rich, powerful etc."},
        "assess": {"pos": "v.", "zh": "評估；評價", "def": "to make a judgment"},
        "medical": {"pos": "adj.", "zh": "醫療的", "def": "relating to medicine and the treatment of disease or injury"},
        "military": {"pos": "adj.", "zh": "軍事的", "def": "associated with soldiers or the military"},
        "package": {"pos": "n.", "zh": "包裹", "def": "a collection of things wrapped or boxed together"},
        "rapid": {"pos": "adj.", "zh": "快速的；迅速的", "def": "happening or done very quickly"},
        "sufficient": {"pos": "adj.", "zh": "足夠的；充分的", "def": "as much as is needed for a particular purpose"},
        "survey": {"pos": "n.", "zh": "調查；測量", "def": "a set of questions that you ask a large number of people in order to find out about their opinions or behaviour"}
    },
    "Unit 10: All in the Mind": {
        "conscious": {"pos": "adj.", "zh": "有意識的；意圖的", "def": "intentionally conceived"},
        "emotion": {"pos": "n.", "zh": "情緒；強烈的情感", "def": "a strong human feeling"},
        "flexible": {"pos": "adj.", "zh": "具彈性的；靈活的", "def": "able to change or be changed easily according to the situation"},
        "function": {"pos": "v.", "zh": "運作；起作用", "def": "to work in the correct or intended way"},
        "perspective": {"pos": "n.", "zh": "看法；觀點", "def": "a particular way of considering something"},
        "reinforce": {"pos": "v.", "zh": "加強；強化", "def": "to make something stronger"},
        "structure": {"pos": "n.", "zh": "結構；建築物", "def": "something that has been built"},
        "transform": {"pos": "v.", "zh": "徹底改變；轉變", "def": "to change completely the appearance or character of something or someone"},
        "vast": {"pos": "adj.", "zh": "巨大的；廣闊的", "def": "very great in size, amount, or extent"},
        "welfare": {"pos": "n.", "zh": "福祉；身心健康", "def": "physical and mental health and happiness"},
        "abstract": {"pos": "adj.", "zh": "抽象的", "def": "existing as an idea or feeling, not as a material object"},
        "acknowledge": {"pos": "v.", "zh": "承認；認知", "def": "to accept, admit or recognize the truth or existence of something"},
        "dismiss": {"pos": "v.", "zh": "不予考慮；摒棄；解散", "def": "to decide that something or someone is not important and not worth considering"},
        "imitate": {"pos": "v.", "zh": "模仿", "def": "to copy the way someone behaves, speaks, moves"},
        "master": {"pos": "v.", "zh": "精通；掌握", "def": "to learn how to do something well"},
        "motive": {"pos": "n.", "zh": "動機；原因", "def": "the reason that makes someone do something, especially when this reason is kept hidden"},
        "possess": {"pos": "v.", "zh": "擁有；具有", "def": "to have a particular quality or ability"},
        "primitive": {"pos": "adj.", "zh": "原始的；簡陋的", "def": "living conditions that are basic, unpleasant and uncomfortable"},
        "pronounce": {"pos": "v.", "zh": "發音；宣佈", "def": "to say a word or a letter in a particular way"},
        "theory": {"pos": "n.", "zh": "理論；學說", "def": "an idea or set of ideas that is intended to explain something about life or the world, especially an idea that has not yet been proved to be true"}
    }
}

st.set_page_config(page_title="Unit 9 & 10 單字複習系統", page_icon="🧠", layout="centered")

st.title("🧠 Unit 9 & 10 單字複習系統")
st.write("透過「看英文選中文」與「看中文拼英文」模式，高效複習高科技與大腦認知單字！")

# 側邊欄設定
st.sidebar.header("⚙️ 設定練習範圍")
unit_choice = st.sidebar.selectbox("選擇單元", ["全部單元", "Unit 9: High-Tech Solutions", "Unit 10: All in the Mind"])
mode_choice = st.sidebar.radio("練習模式", ["看英文選中文 (多選題)", "看中文拼英文 (填空題)"])

# 建立當前單字庫
current_words = {}
if unit_choice == "全部單元":
    current_words.update(WORD_BANK["Unit 9: High-Tech Solutions"])
    current_words.update(WORD_BANK["Unit 10: All in the Mind"])
else:
    current_words.update(WORD_BANK[unit_choice])

word_list = list(current_words.keys())

# 初始化 Session State 變數
if "current_question_word" not in st.session_state or st.session_state.get("prev_unit") != unit_choice:
    st.session_state.current_question_word = random.choice(word_list)
    st.session_state.prev_unit = unit_choice
    st.session_state.answered = False
    st.session_state.is_correct = False
    st.session_state.wrong_ans = ""
    st.session_state.user_score = 0
    st.session_state.total_questions = 0
    st.session_state.options = []

q_word = st.session_state.current_question_word
q_info = current_words[q_word]

# 重新出題函數
def next_question():
    st.session_state.current_question_word = random.choice(word_list)
    st.session_state.answered = False
    st.session_state.is_correct = False
    st.session_state.wrong_ans = ""
    st.session_state.options = []

# --- 模式一：看英文選中文 (多選題) ---
if mode_choice == "看英文選中文 (多選題)":
    st.subheader("請選出該英文單字正確的中文意思：")
    st.info(f"👉 英文單字：**{q_word}** ({q_info['pos']})")
    
    # 產生中文多選題選項
    if not st.session_state.options:
        correct_zh = q_info['zh']
        wrong_zhs = [current_words[w]['zh'] for w in word_list if w != q_word]
        sampled_wrong = random.sample(wrong_zhs, min(3, len(wrong_zhs)))
        options = sampled_wrong + [correct_zh]
        random.shuffle(options)
        st.session_state.options = options

    # 顯示選項按鈕
    for idx, opt in enumerate(st.session_state.options):
        if st.button(f"✨ {opt}", key=f"btn_{opt}", use_container_width=True):
            if not st.session_state.answered:
                st.session_state.answered = True
                st.session_state.total_questions += 1
                if opt == q_info['zh']:
                    st.success(f"🎉 答對了！\n\n📖 課本英文定義：*{q_info['def']}*")
                    st.session_state.user_score += 1
                else:
                    st.error(f"❌ 答錯囉！正確答案是：**{q_info['zh']}**\n\n📖 課本英文定義：*{q_info['def']}*")

# --- 模式二：看中文拼英文 (填空題) ---
else:
    st.subheader("請根據中文提示，輸入正確的英文單字：")
    st.info(f"**中文意思 ({q_info['pos']})**：{q_info['zh']}")
    st.caption(f"📖 英文課本定義：*{q_info['def']}*")
    
    hint = f"💡 提示：字首為 '{q_word[0]}', 字尾為 '{q_word[-1]}', 總共 {len(q_word)} 個字母"
    st.caption(hint)
    
    with st.form(key="input_form", clear_on_submit=True):
        user_input = st.text_input("請輸入英文單字：").strip().lower()
        submit_btn = st.form_submit_button("提交答案")
        
        if submit_btn:
            if not st.session_state.answered:
                st.session_state.answered = True
                st.session_state.total_questions += 1
                if user_input == q_word.lower():
                    st.session_state.is_correct = True
                    st.session_state.user_score += 1
                else:
                    st.session_state.is_correct = False
                    st.session_state.wrong_ans = user_input

    if st.session_state.answered:
        if st.session_state.is_correct:
            st.success(f"🎉 太厲害了！完全正確：**{q_word}**")
        else:
            st.error(f"❌ 拼錯囉！你輸入的是 '{st.session_state.wrong_ans}'，正確答案是：**{q_word}**")

# --- 共用控制與計分板 ---
st.divider()
col1, col2 = st.columns([3, 1])

with col1:
    if st.session_state.answered:
        st.button("下一題 ➡️", on_click=next_question, type="primary")
    else:
        st.button("跳過此題 ⏭️", on_click=next_question)

with col2:
    st.metric("目前得分", f"{st.session_state.user_score} / {st.session_state.total_questions}")

# 單字列表對照表
with st.expander("📚 查看當前範圍的所有單字一覽表"):
    for w in sorted(word_list):
        st.write(f"**{w}** ({current_words[w]['pos']}) 👉 {current_words[w]['zh']}")
