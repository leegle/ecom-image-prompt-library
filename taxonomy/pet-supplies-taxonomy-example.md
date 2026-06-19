# Pet Supplies Taxonomy Example / 宠物用品 分类树示例

Source: public marketplace category framework and user-provided Best Sellers screenshots.

公开仓库只记录通用分类和产品类型，不保存品牌、ASIN、价格、评论数、卖家工具数据或真实商品图片。

## Level Structure / 层级结构

```text
Amazon Best Sellers
└── Pet Supplies / 宠物用品
    ├── Cats / 猫用品
    │   └── cat toy
    │   └── cat water fountain
    │   └── cat grooming brush
    ├── Dogs / 狗用品
    │   └── dog leash
    │   └── dog harness
    │   └── dog grooming brush
    ├── Fish & Aquatic Pets / 鱼与水族宠物
    │   └── aquarium filter
    │   └── fish food
    │   └── aquarium decoration
    ├── Birds / 鸟用品
    │   └── bird feeder
    │   └── bird cage accessory
    ├── Small Animals / 小宠用品
    │   └── hamster toy
    │   └── small animal bedding
```

## Category Nodes / 分类节点

| L2 English | L2 中文 | Suggested Product Types | GitHub Folder |
|---|---|---|---|
| Cats | 猫用品 | cat toy, cat water fountain, cat grooming brush | `cases/pet-supplies/cats/` |
| Dogs | 狗用品 | dog leash, dog harness, dog grooming brush | `cases/pet-supplies/dogs/` |
| Fish & Aquatic Pets | 鱼与水族宠物 | aquarium filter, fish food, aquarium decoration | `cases/pet-supplies/fish-and-aquatic-pets/` |
| Birds | 鸟用品 | bird feeder, bird cage accessory | `cases/pet-supplies/birds/` |
| Small Animals | 小宠用品 | hamster toy, small animal bedding | `cases/pet-supplies/small-animals/` |

## Compliance Notes / 合规注意

- Do not include private brand names, ASINs, prices, review counts, or copied product images.
- Do not add fake badges, fake certifications, fake ratings, or marketplace logos.
- Do not invent unconfirmed performance claims, dimensions, compatibility, or certifications.
