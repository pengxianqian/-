import random

word_dic={
          'robe':'n.长袍，礼服 V.穿',
          'loyalty':'n.忠诚；归属感',
          'domestic':'adj.国内的；家用的 n.家仆；家庭纷争',
          'sword':'n.剑，刀',
          'beast':'n.野兽',
          'steel':'n.钢 v.下决心应对 adj.钢的',
          'steal':'v.偷盗；悄悄移动 n.便宜货',
          'emerge':'vi.浮现；兴起；显露',
          'dull':'adj.无趣的；枯燥的 v.缓和；变钝',
          'barrier':'n.障碍；界线',
          'concentrate':'v.全神贯注于 n.浓缩物',
          'cotton':'n.棉花；棉织品 v.理解；亲近',
          'bow':'vi.点头 vt.低头 v.使弯曲 n.鞠躬',
          'disguise':'n.伪装；化妆用具 v.伪装；装扮',
          'germ':'n.细菌；微生物；萌芽',
          'inquiry':'n.询问；打听',
          'hatch':'vi.孵 n.孵化 v.策划；使孵出',
          'vigorous':'adj.有活力的；强健的',
          'contraty':'adj.对立的；矛盾的 n.相反',
          'fierce':'adj.凶猛的；恶劣的；极端的',
          'distinguish':'v.区别；区分',
          'rejoice':'v.感到高兴',
          'excessive':'adj.过分的；过度的',
          'indifferent':'adj.不感兴趣的；冷漠的',
          'numerous':'adj.为数众多的；许多的',
          'mild':'adj.温和的',
          'poverty':'n.贫困；贫乏'
          }
word_list = [i for i in word_dic.keys()]

if __name__ == '__main__':
    while True:
        word = random.choice(word_list)
        print(word_dic[word])
        Word = None
        while Word != word:
            Word = input('请输入英文：')
            if Word != word:
                print('回答错误！')
        print('下一题')
        print('------------------')
