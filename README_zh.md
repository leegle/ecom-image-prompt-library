# ecom-image-prompt-library

当前版本：**v0.0.1**

这是一个面向跨境电商卖家、设计师和 AI 创作者的商品图片提示词实战库。

项目目标是整理：

- Amazon 类目分类树
- 电商图片提示词模板
- 主图 / 场景图 / 卖点图 / 尺寸图 / A+ 图 / 广告图提示词
- 中英文双语提示词
- 生成图片后的质量检查规则
- 防止六宫格、九宫格、拼图的工作流
- 公开仓库与私有资料分离规则

## 授权协议

CC BY-NC 4.0

个人学习、教育、非商业使用免费。  
商业使用需要单独授权。

## 新手阅读顺序

1. `README_zh.md`
2. `DIRECTORY_zh.md`
3. `VERSIONING.md`
4. `workflow/one-image-per-prompt.md`
5. `workflow/anti-collage-rules.md`
6. `workflow/quality-checklist.md`
7. `prompts/main-image.md`
8. `cases/README.md`

## 公开仓库不要放

- 真实品牌名
- ASIN
- Amazon 后台截图
- 广告报表
- 销售数据
- 成本利润数据
- 供应商信息
- 客户信息
- 竞品图片原图
- 未授权 Logo

公开库建议使用变量：

```text
{brand_name}
{product_name}
{product_type}
{size}
{material}
{usage_scene}
```
