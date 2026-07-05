# 双灶电陶炉：从普通 Amazon 副图到 Apple-inspired 极简高级电商图

> **Dual-Burner Cooktop · Before & After Prompt Case Study**  
> `leegle-image-prompts` 实战案例 · **v0.0.3**
>
> 本案例不是教你“把背景改白”，而是完整演示：  
> **如何把一套信息密集、说明书式的旧 Amazon 副图，转换成更简洁、更高级、更适合高端电商展示的 Apple-inspired 商品视觉。**

---

## 一句话先看懂这个案例

```text
旧图 = 产品事实 + 功能卖点 + 场景信息
新风格 = 构图规则 + 留白 + 光影 + 信息层级 + 文案克制

旧图不是直接照抄。
旧图用来告诉 AI：“这个产品是什么、功能是什么、要表达什么。”

Apple-inspired 风格口令用来告诉 AI：
“应该怎样重新组织这些信息、怎样构图、怎样打光、怎样排版。”
```

最终逻辑：

```text
上传旧图
   ↓
识别旧图核心卖点
   ↓
删除复杂表格 / 长说明 / 多余图标
   ↓
一次只保留一个主卖点
   ↓
加入 Apple-inspired 极简视觉规则
   ↓
生成新图
   ↓
检查产品结构、参数和文字
```

---

# 1. 案例产品

## 产品类型

```text
Dual-Burner Electric Cooktop
双灶电陶炉 / 双区辐射电陶炉
```

## 产品核心视觉特征

- 黑色玻璃面板
- 超薄矩形机身
- 左右两个圆形红色辐射加热区
- 前置触控区域
- 红色数字显示
- 银灰色机身侧边与散热结构
- 台面式 / 嵌入式使用逻辑
- 双区功率分配
- 4 小时定时
- Child Lock
- Hot Surface / Residual Heat Reminder
- 多种平底锅具兼容
- 8 Power Levels
- 8 Cooking Functions

---

# 2. 本案例使用的风格名称

## 中文

```text
苹果启发式极简高级电商产品图风格
```

## English

```text
Apple-inspired minimalist premium product image style
```

> 注意：这里学习的是**极简产品页视觉语言**，不是复制 Apple 的 Logo、官方图片、具体网页或受保护的品牌素材。

---

# 3. 为什么旧图需要重做

旧图并不是“没有信息”。

恰恰相反，旧图的问题通常是：

```text
信息太多
参数太多
说明太长
同一张图表达太多卖点
字体层级混乱
多个圆形放大图
复杂表格
促销色块过多
画面像说明书
产品不是唯一视觉主体
```

传统副图常见结构：

```text
大标题
+ 一段说明
+ 一张产品场景
+ 一个插头放大图
+ 一个圆形控制面板放大图
+ 参数表
+ 多个颜色
```

Apple-inspired 改造逻辑：

```text
一个核心卖点
+ 一个主产品
+ 一句主标题
+ 一句副标题
+ 最少必要参数
+ 大面积留白
+ 柔和自然光
+ 高级商业摄影
```

---

# 4. 通用 Apple-inspired 风格口令

## 中文风格口令

```text
采用 Apple-inspired 极简高级电商产品图风格。整体为浅灰白或暖白背景，大面积留白，产品主体突出，画面安静、克制、现代。使用柔和自然光或高级棚拍光线，黑色玻璃材质具有真实细腻反光。文字使用现代无衬线字体，主标题黑色或深灰色，副标题灰色，排版简洁。单张图片只表达一个核心卖点，只保留必要参数，避免说明书式设计。整体像高端科技品牌官网产品页与高级商业摄影结合的视觉效果。
```

## English style prompt

```text
Use an Apple-inspired minimalist premium product image style. Create a calm, refined, modern composition with a clean light gray, warm white, or soft neutral background and generous negative space. Make the product the dominant visual subject. Use soft natural light or premium studio lighting, realistic black glass reflections, clean modern sans-serif typography, black or dark gray headlines, subtle gray subtext, restrained feature communication, and one clear selling point per image. The final result should feel like a premium technology product page combined with high-end commercial product photography.
```

---

# 5. Before & After 总览

| Case | 旧图表达 | 新图表达 | 核心改造 |
|---|---|---|---|
| 01 | 双灶功率分配 + 插头 + 长说明 + 表格 | Shared 2000W Power | 删除表格，只保留 1600W / 400W |
| 02 | 4 小时定时 + 三行操作说明 | Up to 4-Hour Timer | 变成 3 步极简操作 |
| 03 | 清洁 + Child Lock + Residual Heat | Easy to Clean | 主场景突出清洁，两个安全点做辅助 |
| 04 | 8 种锅具缩略图 + 大场景 | Compatible with Daily Cookware | 六种锅具统一卡片化 |
| 05 | 控制面板 + 8 张食物拼图 | 8 Power Levels / 8 Cooking Functions | 信息分层，食物卡片统一 |
| 06 | 台面 / 嵌入 + 底部结构 + 大量尺寸箭头 | Flexible Installation | 两种安装方式上下对比 |

---

# 6. Case 01 · Shared 2000W Power

## 旧图

![Old Shared 2000W Power](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/old/01-shared-2000w-power-old.jpg)

## 新图

![New Shared 2000W Power](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/new/01-shared-2000w-power-new.png)

## 旧图主要问题

旧图同时出现：

- “Dual Burner Intelligent Power Adjustment”
- Shared 2000W
- 插头局部图
- 110–120V
- 一大段功率说明
- 左右功率完整表格
- 双锅场景

信息全部挤在一张图中。

用户需要先“读图”，才能理解产品。

## 新图改造逻辑

新图只回答一个问题：

> **两个炉区同时工作时，2000W 功率如何分配？**

只保留：

```text
Smart Dual-Zone Cooking
Shared 2000W Power

Left Zone
1600W

Right Zone
400W
```

用两条极简指示线直接连接左右炉区。

## 新图优点

1. **3 秒内理解卖点**  
   左 1600W、右 400W，一眼看懂。

2. **产品成为视觉主体**  
   不再被表格和插头图抢视觉。

3. **真实场景更强**  
   左侧炖煮、右侧煎牛排，直接表现双灶同时工作。

4. **功率信息和使用场景建立联系**  
   参数不再只是数字，而是与左右炉区对应。

5. **更适合 Amazon 手机端浏览**  
   大标题、大数字、少文字。

## 中文生成提示词

```text
生成一张 Amazon 副图风格的高级电商产品图片，目标尺寸 2048×2048 px，采用 Apple-inspired 极简高级电商产品图风格。

画面主体是一台现代双灶电陶炉，黑色玻璃面板、超薄矩形机身、两个圆形红色辐射加热区、前置触控区域和银灰色侧边散热结构。保持双灶产品结构真实、完整，不改变左右炉区数量和基本比例。

产品放置在现代浅灰白厨房石材台面上，采用正面略微俯视的高级产品摄影视角。左侧炉区放置黑色双耳汤锅，锅中正在炖煮丰富食材，有轻微自然蒸汽。右侧炉区放置黑色平底锅，锅中煎制牛排，同样有轻微自然蒸汽。左右两个红色加热区同时工作。

顶部只保留两行主文案：

Smart Dual-Zone Cooking
Shared 2000W Power

在左侧锅上方加入极简功率标签：

Left Zone
1600W

在右侧平底锅上方加入极简功率标签：

Right Zone
400W

使用非常细的深灰色垂直指示线，将两个功率标签分别连接到对应炉区。不要复杂功率表，不要插头放大图，不要长段说明，不要额外参数。

背景为明亮现代浅色厨房，暖白墙面、浅色石材台面、大面积留白、柔和自然光。产品黑色玻璃表面具有真实自然反光，红色发热区域清晰但不过度发光。

字体使用现代无衬线字体，主标题黑色粗体，功率数字清晰，整体排版克制、高级、安静。

不要复杂表格，不要参数堆砌，不要大量小字，不要促销横幅，不要圆形功能放大图，不要杂乱图标，不要拼图，不要说明书式排版，不要低端海报感。
```

## English prompt

```text
Create a premium Amazon secondary image, targeting a 2048x2048 square composition, in an Apple-inspired minimalist premium product image style.

The hero product is a modern dual-burner electric radiant cooktop with a black glass surface, ultra-slim rectangular body, two circular red radiant heating zones, a front touch control area, and a silver-gray ventilated side structure. Preserve the realistic dual-zone structure and product proportions.

Place the cooktop on a light gray-white stone countertop in a bright modern kitchen. Use a clean frontal view with a slightly elevated camera angle. On the left cooking zone, place a matte black stock pot simmering a rich stew with gentle natural steam. On the right cooking zone, place a black frying pan searing a steak with subtle steam. Both red radiant zones are operating at the same time.

Top text only:

Smart Dual-Zone Cooking
Shared 2000W Power

Above the left zone, add a minimal label:

Left Zone
1600W

Above the right zone, add a minimal label:

Right Zone
400W

Use thin dark gray vertical guide lines to connect each power label to its corresponding cooking zone. Do not show a complex power table, plug inset, long explanation, or extra technical parameters.

Use a bright neutral kitchen background, warm white walls, pale stone countertop, generous negative space, and soft natural light. Render realistic refined reflections on the black glass surface. Keep the red radiant glow clear but restrained.

Use clean modern sans-serif typography, a bold black headline, clear power numbers, and a calm premium layout.

No complex tables, no parameter overload, no tiny text, no promotional banners, no circular magnifier insets, no cluttered icon groups, no collage, no manual-style layout, no cheap advertising look.
```

---

# 7. Case 02 · Up to 4-Hour Timer

## 旧图

![Old 4-Hour Timer](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/old/02-four-hour-timer-old.jpg)

## 新图

![New 4-Hour Timer](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/new/02-four-hour-timer-new.png)

## 旧图主要问题

旧图顶部直接写完整操作说明：

```text
1. Select the burner...
2. Press the timer...
3. Press the Timer button...
```

问题是：

- 阅读成本高
- 小字过多
- 英文说明像用户手册
- 圆形放大图与场景抢视觉
- 4-hour 核心卖点不够突出

## 新图改造逻辑

把长说明压缩为三个动作：

```text
1 Select Zone
2 Tap Timer
3 Set Time
```

同时保留一个大号 `4:00` 控制区域特写。

## 新图优点

- 首屏首先看到 **Up to 4-Hour Timer**
- 用户不用阅读说明书
- 三步流程适合手机端
- `4:00` 视觉证据直接
- 产品仍是主画面，不是 UI 教程截图

## 中文生成提示词

```text
生成一张 Amazon 副图，目标尺寸 2048×2048 px，采用 Apple-inspired 极简高级电商产品图风格。

画面主体是一台现代双灶电陶炉，黑色玻璃面板、两个红色辐射加热区、前置触控区域和银灰色散热机身。产品放在明亮现代浅色厨房台面上。

左侧炉区放黑色汤锅，锅中炖煮牛肉和蔬菜，有柔和蒸汽。右侧炉区放黑色平底锅，煎制牛排和小番茄，有少量蒸汽。画面真实、温暖、干净。

左上方放置大标题：

Up to 4-Hour Timer

副标题：

Simple Preset Cooking

标题下方只使用三个极简步骤：

1
Select Zone

2
Tap Timer

3
Set Time

三个步骤横向排列，使用细灰色分隔线，黑色现代无衬线字体。

画面右上方加入一个单独的圆形控制面板特写，仅显示简洁的 Timer 图标、4:00 红色数字和 Hot Surface 提示。圆形特写必须简洁、高清、像高端科技产品功能展示，不要增加其他复杂控制元素。

产品主体占据画面下半部分，背景保留大面积暖白留白。柔和自然光，高级商业摄影质感，黑色玻璃反光细腻真实。

不要完整说明书步骤，不要长段英文，不要复杂按钮说明，不要多个圆形放大图，不要促销横幅，不要低端广告风，不要拼图。
```

## English prompt

```text
Create a premium Amazon secondary image, targeting a 2048x2048 square format, in an Apple-inspired minimalist premium product style.

Feature a modern dual-burner radiant electric cooktop with a black glass surface, two red radiant heating zones, a front touch control area, and a silver-gray ventilated body. Place it on a bright neutral kitchen countertop.

On the left zone, show a matte black stock pot simmering beef and vegetables with soft natural steam. On the right zone, show a black frying pan searing steak and small tomatoes with subtle steam. Keep the cooking scene realistic, warm, and clean.

Place a large headline in the upper left:

Up to 4-Hour Timer

Subtitle:

Simple Preset Cooking

Below the title, show only three minimal horizontal steps:

1
Select Zone

2
Tap Timer

3
Set Time

Separate the three steps with thin light-gray vertical lines. Use clean black modern sans-serif typography.

In the upper right, add one clean circular close-up of the control area. Show only a minimal Timer icon, a red 4:00 digital display, and a subtle Hot Surface indicator. The circular close-up should feel like a premium technology feature detail, clean and high resolution.

Keep the cooktop as the main subject in the lower half of the image. Preserve generous warm-white negative space, soft natural lighting, premium commercial photography, and refined black glass reflections.

No full manual instructions, no long paragraphs, no complicated button explanations, no multiple circular magnifiers, no promotional banner, no cheap advertising style, no collage.
```

---

# 8. Case 03 · Easy to Clean

## 旧图

![Old Easy to Clean](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/old/03-easy-to-clean-old.jpg)

## 新图

![New Easy to Clean](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/new/03-easy-to-clean-new.png)

## 旧图主要问题

旧图同时讲：

- Easy to clean
- Light blinks when plugged in
- Child Lock
- Residual heat
- 一个大清洁场景
- 三个圆形 / 方形局部图

卖点过多，层级不清晰。

## 新图改造逻辑

新图把主卖点固定为：

```text
Easy to Clean
```

安全功能只作为辅助：

```text
Child Lock
Hot Surface
```

## 新图优点

- 清洁动作成为第一视觉证据
- 安全功能作为次级信息，不抢主标题
- 两个圆形模块对称统一
- 删除“Light blinks when plugged in”等弱卖点
- 画面更像产品页，而不是说明书

## 中文生成提示词

```text
生成一张 2048×2048 px 的 Amazon 副图，采用 Apple-inspired 极简高级电商产品图风格。

画面主体是一台现代双灶电陶炉，黑色玻璃面板、两个圆形红色辐射加热区、前置触控区域。产品放置在干净的浅灰白石材厨房台面上。

画面表现“易清洁”核心卖点。一只戴浅色清洁手套的手，使用折叠整齐的柔软黄色超细纤维布，轻轻擦拭右侧黑色玻璃面板。擦拭动作自然，重点表现平整光滑玻璃表面和易于日常清洁的视觉效果。

顶部大标题：

Easy to Clean

副标题：

Child Lock • Residual Heat Reminder

画面下方只保留两个简洁圆形功能模块。

左侧圆形模块：
显示简洁锁定图标和文字：

Lock (3 sec)

圆形模块下方文字：

Child Lock

右侧圆形模块：
显示一个小型橙红色提示灯和文字：

Hot Surface

圆形模块下方文字：

Hot Surface

整体背景暖白、浅灰、高级、干净。使用大面积留白、柔和自然光、细腻玻璃反光、现代无衬线字体。主标题黑色粗体，副标题深灰色。

不要加入插电提示，不要多个杂乱功能放大图，不要橙色大色块，不要长段说明，不要促销风，不要复杂图标堆砌，不要说明书式排版。
```

## English prompt

```text
Create a 2048x2048 Amazon secondary image in an Apple-inspired minimalist premium product image style.

The hero product is a modern dual-burner electric radiant cooktop with a black glass surface, two circular red radiant heating zones, and a front touch control area. Place it on a clean light gray-white stone kitchen countertop.

The primary selling point is easy cleaning. Show one hand wearing a light-colored cleaning glove gently wiping the right side of the black glass cooktop with a neatly folded soft yellow microfiber cloth. Make the wiping action natural and clearly communicate a smooth flat glass surface suitable for simple everyday cleaning.

Top headline:

Easy to Clean

Subtitle:

Child Lock • Residual Heat Reminder

At the bottom, show only two clean circular feature modules.

Left circular module:
A minimal lock icon and the text:

Lock (3 sec)

Below the circle:

Child Lock

Right circular module:
A small warm orange-red indicator light and the text:

Hot Surface

Below the circle:

Hot Surface

Use a warm white and light gray environment, generous negative space, soft natural lighting, refined glass reflections, and clean modern sans-serif typography. Use a bold black headline and dark gray subtitle.

No plug-in indicator feature, no multiple cluttered magnifier insets, no large orange promotional blocks, no long paragraphs, no promotional poster style, no icon overload, no manual-style layout.
```

---

# 9. Case 04 · Compatible with Daily Cookware

## 旧图

![Old Cookware Compatibility](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/old/04-cookware-compatibility-old.jpg)

## 新图

![New Cookware Compatibility](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/new/04-cookware-compatibility-new.png)

## 旧图主要问题

旧图使用 8 个锅具小图，并叠加：

- Cast iron cookware
- Stainless steel cookware
- Concave base cookware
- Enameled iron cookware
- Aluminum cookware
- Copper cookware
- Ceramic cookware
- Glass cookware

同时背景还有完整厨房和双锅场景。

结果是视觉非常满。

## 新图改造逻辑

把锅具兼容性改成统一的 2×3 卡片：

```text
Cast Iron
Stainless Steel
Ceramic
Glass
Enamel
Aluminum
```

底部只用一个双灶真实烹饪场景做“实际使用证明”。

## 新图优点

- 锅具类型更容易扫读
- 卡片尺寸统一
- 每个锅具独立展示
- 背景颜色统一
- 信息与产品使用场景上下分层
- 避免传统拼贴海报感

## 中文生成提示词

```text
生成一张 2048×2048 px 的 Amazon 副图，采用 Apple-inspired 极简高级电商产品图风格。

主题是双灶电陶炉的日常锅具兼容性。

顶部大标题：

Compatible with Daily Cookware

副标题：

Works with many flat-bottom pots and pans

画面上半部分使用六个统一尺寸、统一圆角、暖白半透明背景的极简产品卡片，以 3 列 × 2 行整齐排列。

六个卡片分别展示：

Cast Iron
黑色铸铁锅

Stainless Steel
银色不锈钢锅

Ceramic
米白色陶瓷锅

Glass
透明玻璃锅

Enamel
浅色珐琅锅

Aluminum
银色铝制奶锅

每个卡片只展示一个锅具，产品居中，背景干净，底部使用黑色现代无衬线字体标注英文锅具名称。六个卡片的摄影角度、光线和比例保持统一。

画面下半部分展示一台现代双灶电陶炉放置在高级暖色现代厨房台面上。左侧炉区使用不锈钢双耳汤锅炖煮食材，右侧炉区使用黑色平底锅煎牛排。两个红色辐射加热区正在工作，有少量自然蒸汽。

整体使用暖白、米灰、浅木色背景，柔和自然光，大面积留白，高级商业摄影质感。产品玻璃表面反光真实、克制。

不要使用八个以上锅具缩略图，不要橙色标签条，不要复杂拼贴，不要杂乱厨房，不要长段说明，不要夸大兼容所有锅具。文案表达使用“many flat-bottom pots and pans”。
```

## English prompt

```text
Create a 2048x2048 Amazon secondary image in an Apple-inspired minimalist premium product image style.

The theme is everyday cookware compatibility for a dual-burner radiant electric cooktop.

Top headline:

Compatible with Daily Cookware

Subtitle:

Works with many flat-bottom pots and pans

In the upper half, create six consistent minimalist product cards arranged in a clean 3-column by 2-row grid. Use identical rounded corners and soft warm-white translucent card backgrounds.

The six cards show:

Cast Iron
a matte black cast iron pot

Stainless Steel
a polished silver stainless steel pot

Ceramic
a warm off-white ceramic pot

Glass
a transparent glass cooking pot

Enamel
a light-colored enamel pot

Aluminum
a brushed silver aluminum saucepan

Show only one cookware item per card. Center each item, use consistent product photography angles, consistent lighting, and consistent scale. Add the cookware name in clean black modern sans-serif text at the bottom of each card.

In the lower half, show a modern dual-burner radiant cooktop on a premium warm neutral kitchen countertop. Use a stainless steel stock pot simmering food on the left zone and a black frying pan searing steak on the right zone. Both red radiant heating zones are active with subtle natural steam.

Use a warm white, beige-gray, and light wood interior, soft natural lighting, generous negative space, premium commercial photography, and realistic restrained glass reflections.

No eight-plus thumbnail collage, no orange label bars, no cluttered montage, no busy kitchen, no long paragraph, and do not claim universal cookware compatibility. Use the wording “many flat-bottom pots and pans.”
```

---

# 10. Case 05 · 8 Power Levels / 8 Cooking Functions

## 旧图

![Old Power Levels and Functions](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/old/05-power-levels-functions-old.jpg)

## 新图

![New Power Levels and Functions](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/new/05-power-levels-functions-new.png)

## 旧图主要问题

旧图信息逻辑其实是正确的：

```text
控制区
+
8 cooking functions
```

但存在几个问题：

- 顶部橙色横幅过强
- “8 Power level,8 Cooking Functions”语法和标点不够高级
- 8 张食物图片边界杂乱
- 整体像低价促销页
- 主产品结构被裁切得过多

## 新图改造逻辑

上半部分：

```text
8 Power Levels
8 Cooking Functions
```

使用一个控制区高清特写。

下半部分：

```text
Melt
Simmer
Steam
Boil
Fry
Roast
Stir-Fry
Fast Heat
```

统一成 2×4 卡片。

## 新图优点

- 核心数字 `8` 成为视觉锚点
- 控制区与功能卡片信息分层
- 8 个功能卡片统一尺寸和背景
- 食物摄影风格统一
- 更适合形成模板，后续换其他小家电也能复用

## 中文生成提示词

```text
生成一张 2048×2048 px 的 Amazon 副图，采用 Apple-inspired 极简高级电商产品图风格。

主题是：

8 Power Levels
8 Cooking Functions

画面上半部分展示双灶电陶炉左侧炉区和触控控制区域的高级近景特写。产品为黑色玻璃面板，红色辐射发热圈清晰，黑色玻璃具有自然细腻反光。控制区显示红色数字 1600，并保留极简的 Lock、Timer、减号、加号、Function 和 On/Off 视觉逻辑。控制面板结构清晰但不要增加额外小字。

右上方标题排版：

8 Power Levels

其中数字 8 使用克制的暖橙红色，Power Levels 使用黑色粗体现代无衬线字体。

下一行副标题：

8 Cooking Functions

使用深灰色字体。

画面下半部分使用 4 列 × 2 行的八个统一圆角功能卡片。

卡片分别为：

Melt
融化的巧克力

Simmer
低温炖煮的汤

Steam
竹蒸笼中的蒸饺

Boil
不锈钢锅中沸腾的水

Fry
黑色平底锅煎鸡蛋

Roast
煎烤牛排

Stir-Fry
彩色蔬菜和虾仁翻炒

Fast Heat
抽象红色辐射加热圈与向上热量箭头

八个卡片尺寸完全统一，暖白或浅灰背景，食物主体居中，顶部只保留对应英文功能名称。整体摄影风格统一、高级、真实。

不要橙色大横幅，不要黑色粗重拼图边框，不要杂乱食物拼贴，不要低端促销风，不要增加无关参数，不要大量小字。
```

## English prompt

```text
Create a 2048x2048 Amazon secondary image in an Apple-inspired minimalist premium product image style.

The theme is:

8 Power Levels
8 Cooking Functions

In the upper half, show a premium close-up of the left cooking zone and touch control area of a modern dual-burner radiant electric cooktop. The cooktop has a black glass surface, a clear red radiant heating coil, and refined realistic glass reflections. The control area shows a red 1600 digital display and a minimal visual logic for Lock, Timer, minus, plus, Function, and On/Off. Keep the control layout clean and avoid extra tiny text.

In the upper right, add the headline:

8 Power Levels

Use a restrained warm orange-red color for the number 8 and bold black modern sans-serif typography for “Power Levels.”

Below it, add:

8 Cooking Functions

Use dark gray typography.

In the lower half, create eight identical rounded feature cards arranged in a 4-column by 2-row grid.

The cards are:

Melt
smooth melted chocolate

Simmer
a gently simmering soup

Steam
dumplings in a bamboo steamer

Boil
boiling water in a stainless steel pot

Fry
a fried egg in a black frying pan

Roast
a roasted or seared steak

Stir-Fry
colorful vegetables and shrimp in a wok

Fast Heat
an abstract red radiant heating coil with upward heat arrows

Use identical card sizes, warm-white or light-gray backgrounds, centered food subjects, consistent premium food photography, and only the English function name at the top of each card.

No large orange banner, no heavy black collage borders, no messy food montage, no cheap promotional style, no unrelated parameters, no excessive small text.
```

---

# 11. Case 06 · Flexible Installation

## 旧图

![Old Flexible Installation](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/old/06-flexible-installation-old.jpg)

## 新图

![New Flexible Installation](https://raw.githubusercontent.com/leegle/ecom-image-prompt-library/main/cases/appliances/cooktops/leegle-image-prompts_dual-burner-apple-style-case_v0.0.3/assets/new/06-flexible-installation-new.png)

## 旧图主要问题

旧图同时出现：

- 底部结构
- 四个支脚
- 三组尺寸
- Use On The Countertop
- Built-in Electric Cooktop
- 两个使用场景
- 橙色曲线分区

信息虽然完整，但视觉逻辑复杂。

## 新图改造逻辑

新图只表达：

```text
Flexible Installation
Countertop or Built-In
```

分为上下两个场景：

```text
上：Countertop
下：Built-In
```

尺寸统一使用简洁工程标尺。

## 新图优点

- 台面式和嵌入式一眼区分
- 尺寸标尺简洁
- 产品结构保持统一
- 删除波浪形促销分区
- 4 个支脚作为单独必要信息放到底部
- 更接近高端产品规格页

## 中文生成提示词

```text
生成一张 2048×2048 px 的 Amazon 副图，采用 Apple-inspired 极简高级电商规格图风格。

主题：

Flexible Installation

副标题：

Countertop or Built-In

画面整体采用暖白和浅灰背景，大面积留白，现代无衬线字体，黑色标题，灰色副标题。图片分为上下两个主要区域，但不要使用粗重边框、彩色横幅或波浪分隔。

上半部分展示双灶电陶炉作为 countertop 台面式使用。产品完整放置在浅灰白石材台面上，从正面略微俯视角度展示。产品黑色玻璃面板、两个红色辐射加热区和银灰色侧边散热结构保持真实。

使用极简黑色尺寸标尺显示：

22.4 in

横向标注产品宽度。

左侧使用简洁尺寸标尺显示：

12.6 in

标注产品深度。

右侧使用简洁垂直尺寸标尺显示：

2.0 in

标注产品高度。

下半部分展示同一产品的 built-in 嵌入式安装效果。产品平整嵌入浅色石材台面，保留完整黑色双灶面板。

同样使用极简尺寸标尺显示：

22.4 in

12.6 in

画面最底部单独展示一个黑色支撑脚配件，旁边只保留文字：

4 support feet included

整体像高端科技产品规格页，测量线纤细、准确、简洁，产品比例真实，背景明亮高级。

不要橙色波浪分区，不要大面积促销色块，不要复杂安装说明，不要大量箭头，不要多个杂乱零件，不要说明书式排版。
```

## English prompt

```text
Create a 2048x2048 Amazon secondary image in an Apple-inspired minimalist premium specification-page style.

Theme:

Flexible Installation

Subtitle:

Countertop or Built-In

Use a warm white and light gray background, generous negative space, clean modern sans-serif typography, a black headline, and a gray subtitle. Divide the image into two main vertical sections without heavy borders, colored promotional banners, or curved wave separators.

In the upper section, show the dual-burner electric radiant cooktop in a countertop installation. Place the complete product on a light gray-white stone countertop and show it from a clean frontal angle with slight elevation. Preserve the realistic black glass surface, two red radiant heating zones, and silver-gray ventilated side structure.

Use thin minimal black dimension lines to show:

22.4 in

for the product width.

On the left, show:

12.6 in

for the product depth.

On the right, show:

2.0 in

for the product height.

In the lower section, show the same cooktop in a built-in installation, sitting flush inside a light stone countertop. Preserve the full black dual-zone cooking surface.

Use the same minimal dimension style to show:

22.4 in

and

12.6 in

At the bottom, show one black support foot accessory as a separate clean product detail with the text:

4 support feet included

The final image should feel like a premium technology product specification page. Keep dimension lines thin, accurate, clean, and restrained. Preserve realistic product proportions and a bright premium environment.

No orange wave divider, no large promotional color blocks, no complicated installation instructions, no excessive arrows, no cluttered accessory collection, no manual-style layout.
```

---

# 12. 六张旧图与新图的整体区别

## 12.1 信息量

### 旧图

```text
一张图 = 3～6 个卖点
```

### 新图

```text
一张图 = 1 个核心卖点 + 0～2 个辅助信息
```

---

## 12.2 视觉中心

### 旧图

视觉中心经常在：

```text
橙色标题
表格
圆形放大图
说明文字
食物拼图
```

### 新图

视觉中心始终是：

```text
产品
或
产品正在使用的真实场景
```

---

## 12.3 文案层级

### 旧图

```text
主标题
副标题
说明
步骤
注释
表格
标签
参数
```

### 新图

默认只保留：

```text
主标题
副标题
必要数字
```

特殊功能图最多加入：

```text
3 个步骤
或
6～8 个统一卡片
```

---

## 12.4 色彩

### 旧图

```text
橙色
红色
黑色
白色
厨房暖色
多种食物颜色
```

同时竞争视觉。

### 新图

主视觉色：

```text
暖白
浅灰
黑色
深灰
产品红色发热区
```

橙红色只用于：

```text
数字 8
提示灯
必要强调
```

---

## 12.5 构图

### 旧图

```text
拼贴
大横幅
圆形局部图
表格
说明区
```

### 新图

主要采用：

```text
大产品 Hero
左右对应
上下分区
统一卡片
极简特写
```

---

# 13. 新图最明显的 8 个优点

## 1. 更快理解

Amazon 用户不会逐字阅读副图。

新图采用：

```text
大标题
大数字
明确场景
```

用户可以快速理解。

## 2. 更适合手机端

旧图的小表格、长说明在手机上很难阅读。

新图使用：

```text
1600W
400W
4:00
8
```

作为视觉锚点。

## 3. 产品更高级

黑色玻璃产品最重要的是：

```text
边缘
比例
反光
材质
红色发热状态
```

新图给产品更多展示空间。

## 4. 单图卖点更明确

每张图片只解决一个问题：

```text
功率怎么分配？
定时怎么使用？
是否容易清洁？
兼容哪些锅具？
有多少档位和功能？
怎么安装？
```

## 5. 图片之间风格统一

六张图统一使用：

```text
现代无衬线字体
暖白 / 浅灰背景
黑色产品
深灰副标题
柔和光线
克制排版
```

放在 Amazon Listing 中更像一套完整品牌视觉。

## 6. 更容易模板化

例如 Case 04 的锅具卡片结构，可以直接迁移到：

```text
coffee maker
air fryer
blender
ice maker
portable stove
induction cooktop
```

## 7. 更适合开源提示词案例

旧图很难提炼成模板。

新图可以直接拆成：

```text
产品主体
卖点
场景
信息模块
排版
光线
负面要求
```

## 8. 更适合后续做视频

这六张图已经天然形成视频脚本：

```text
01 双灶同时工作
02 4 小时定时
03 一擦即净 + 安全提示
04 多种锅具
05 8 档 / 8 功能
06 台面式 / 嵌入式
```

---

# 14. 新手怎么把旧图变成这种新图

## 第一步：上传旧图

不要先写长提示词。

先上传旧 Amazon 副图。

例如上传：

```text
Dual Burner Intelligent Power Adjustment, Shared 2000W
```

这张旧图。

---

## 第二步：让 AI 先识别旧图

可以输入：

```text
分析这张 Amazon 副图。

请告诉我：

1. 产品是什么
2. 这张图的核心卖点是什么
3. 哪些参数必须保留
4. 哪些文字可以删除
5. 哪些元素导致画面显得杂乱
6. 如果改成 Apple-inspired 极简高级商品图，应该只保留什么
```

先分析。

不要立即生图。

---

## 第三步：输入风格口令

```text
Apple-inspired minimalist premium product image style
```

或者中文：

```text
苹果启发式极简高级电商产品图风格
```

然后说：

```text
学习这种极简商品视觉逻辑。

不要复制品牌 Logo、官方图片或具体网页素材。

只学习：
留白
构图
光影
字体层级
产品 Hero 展示
极简功能表达
```

---

## 第四步：告诉 AI 只提炼一个卖点

例如旧图有：

```text
Shared 2000W
110-120V
1600W
400W
Power Table
Plug
```

你不要全部生成。

输入：

```text
这张新图只表达 Shared 2000W Power。

保留 Left Zone 1600W 和 Right Zone 400W。

删除插头放大图。
删除 110-120V。
删除完整功率表。
删除长说明。
```

这一步非常重要。

---

## 第五步：要求 AI 先写最终生图提示词

输入：

```text
先不要生成图片。

根据旧图的产品结构和核心卖点，
按照 Apple-inspired 极简高级电商产品图风格，
帮我写一份 2048×2048 px Amazon 副图生图提示词。

提示词必须包括：

1. 产品主体
2. 产品结构
3. 使用场景
4. 核心卖点
5. 允许出现的文字
6. 信息模块
7. 背景
8. 光线
9. 材质
10. 构图
11. 负面要求

单图只表达一个核心卖点。
```

---

## 第六步：检查提示词

重点检查：

```text
产品有没有被改型？
炉区数量对不对？
黑色玻璃面板有没有保留？
参数对不对？
是否删除了复杂表格？
文字是不是太多？
有没有偷偷增加新功能？
```

---

## 第七步：生成

确认提示词后：

```text
按照这个提示词生成。
```

---

## 第八步：二次修正

不要一张图不满意就全部推翻。

按问题修：

### 产品结构错

```text
保持原产品双灶结构不变。
不要改变机身比例。
不要增加第三个炉区。
不要改变前置控制区域位置。
```

### 文字太多

```text
删除所有其他小字。

画面只保留：

[主标题]
[副标题]
[必要参数]
```

### 画面不够高级

```text
增加大面积留白。
减少背景摆件。
背景改为暖白和浅灰。
使用柔和自然光。
降低装饰元素数量。
强化产品 Hero 构图。
```

### 太像说明书

```text
删除表格。
删除长段说明。
删除步骤段落。
删除多个局部放大图。
每张图只表达一个核心卖点。
```

---

# 15. 可复用提示词公式

```text
[目标尺寸]
+
[平台与图片类型]
+
[风格]
+
[产品主体]
+
[必须保持的产品结构]
+
[一个核心卖点]
+
[真实使用场景]
+
[允许出现的文字]
+
[极简信息模块]
+
[背景]
+
[光线]
+
[材质]
+
[构图]
+
[负面要求]
```

示例：

```text
2048×2048
+
Amazon secondary image
+
Apple-inspired minimalist premium product image style
+
dual-burner radiant electric cooktop
+
black glass / two heating zones / front touch controls
+
Shared 2000W Power
+
pot simmering + pan searing steak
+
headline + subtitle + 1600W / 400W
+
thin guide lines
+
light modern kitchen
+
soft natural light
+
realistic refined glass reflections
+
hero composition with negative space
+
no table / no long text / no collage / no promo banner
```

---

# 16. 质量检查清单

生成完成后逐项检查：

## 产品

- [ ] 还是双灶
- [ ] 两个炉区数量正确
- [ ] 黑色玻璃面板正确
- [ ] 超薄矩形机身正确
- [ ] 产品没有被改成电磁炉外观
- [ ] 前置控制区逻辑基本一致
- [ ] 红色辐射加热状态合理

## 功能

- [ ] 2000W 没有写错
- [ ] 1600W / 400W 没有写反
- [ ] 4-Hour Timer 没有变成 24-Hour
- [ ] Child Lock 没有变成其他功能
- [ ] Hot Surface 表达正确
- [ ] 8 Power Levels 正确
- [ ] 8 Cooking Functions 正确
- [ ] 安装尺寸与原始资料一致

## 视觉

- [ ] 主标题清晰
- [ ] 副标题清晰
- [ ] 没有乱码
- [ ] 没有多余小字
- [ ] 没有复杂表格
- [ ] 没有促销横幅
- [ ] 没有大量图标
- [ ] 产品是主视觉
- [ ] 留白充足
- [ ] 整套风格统一

---

# 17. GitHub 推荐目录

```text
cases/
└── appliances/
    └── cooktops/
        └── dual-burner-radiant-cooktop/
            └── apple-inspired-minimalist-product-image-style/
                ├── README.md
                └── assets/
                    ├── old/
                    │   ├── 01-shared-2000w-power-old.jpg
                    │   ├── 02-four-hour-timer-old.jpg
                    │   ├── 03-easy-to-clean-old.jpg
                    │   ├── 04-cookware-compatibility-old.jpg
                    │   ├── 05-power-levels-functions-old.jpg
                    │   └── 06-flexible-installation-old.jpg
                    └── new/
                        ├── 01-shared-2000w-power-new.png
                        ├── 02-four-hour-timer-new.png
                        ├── 03-easy-to-clean-new.png
                        ├── 04-cookware-compatibility-new.png
                        ├── 05-power-levels-functions-new.png
                        └── 06-flexible-installation-new.png
```

---

# 18. 关于图片尺寸

本案例的**目标生图尺寸**是：

```text
2048 × 2048 px
1:1 square
```

当前案例包中保存的新图为本次对话上传的预览文件，文件分辨率为：

```text
1254 × 1254 px
```

因此：

> 提示词仍然按 2048×2048 Amazon 副图目标编写；实际发布到 Amazon 或开源库时，应优先保存原始 2048×2048 生成文件。

---

# 19. 开源说明

本案例用于：

- AI 电商生图学习
- Prompt 结构研究
- Amazon 副图视觉改造教程
- 视觉风格提炼方法演示

请注意：

```text
Apple-inspired
```

表示学习极简产品页的通用视觉语言。

本项目不建议：

- 复制 Apple 官方图片
- 使用 Apple Logo
- 复制 Apple 官网具体页面
- 冒充 Apple 产品
- 直接复制第三方品牌素材作为商业成品

建议公开案例使用：

```text
generic product
unbranded product
brand removed
logo removed
```

---

# 20. 最终总结

这次改造最重要的不是“把旧图变漂亮”。

真正有价值的是建立了一套可以复用的方法：

```text
旧图负责提供事实
↓
AI 负责识别卖点
↓
人工决定单图核心信息
↓
风格口令负责视觉语言
↓
结构化提示词负责生成
↓
人工检查产品和参数
↓
形成可复用案例
```

最核心原则：

> **不要让 AI 自动决定一张图表达多少信息。**

应该由你先决定：

```text
这张图只卖什么？
```

然后提示词围绕这个卖点生成。

对于本案例：

```text
图 01 = Shared 2000W Power
图 02 = 4-Hour Timer
图 03 = Easy to Clean
图 04 = Cookware Compatibility
图 05 = 8 Power Levels / 8 Cooking Functions
图 06 = Countertop or Built-In
```

这就是从“普通 Amazon 功能海报”升级成“高端极简电商产品视觉”的完整逻辑。
