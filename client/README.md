# 🍽️ 스마트 냉장고 앱

**Ultra Premium UI**로 구현된 스마트 냉장고 관리 애플리케이션

## ✨ 주요 기능

### 🥬 내 냉장고
- **식재료 관리**: 보유 식재료 추가, 수정, 삭제
- **유통기한 추적**: 자동 알림 및 상태별 분류 (긴급, 주의, 신선, 만료)
- **영수증 업로드**: AI OCR을 통한 자동 식재료 등록

### 🛒 장바구니  
- **구매 목록 관리**: 구매할 상품 추가 및 관리
- **수량 조절**: 직관적인 +/- 버튼
- **가격 계산**: 실시간 총액 계산

### 👨‍🍳 레시피 추천
- **맞춤 레시피**: 보유 식재료 기반 레시피 추천
- **난이도별 분류**: 쉬움, 보통, 어려움
- **조리시간 표시**: 효율적인 요리 계획

## 🎨 Ultra Premium UI Features

- **🌈 Dynamic Gradient Background**: 10초마다 변화하는 아름다운 배경
- **✨ Glassmorphism Effects**: 32px 블러 + 투명도로 구현된 유리 효과  
- **🎭 Floating Particles**: 배경에 떠다니는 파티클 애니메이션
- **💫 Shimmer Animations**: 로고와 UI 요소의 빛나는 효과
- **🚀 3D Hover Effects**: 카드와 버튼의 입체적 상호작용
- **📱 Perfect Responsive**: 모든 디바이스 완벽 대응

## 🛠️ 기술 스택

- **Frontend**: React 18 + JavaScript
- **Styling**: Custom CSS with Design System
- **Icons**: Lucide React
- **Animations**: Framer Motion + CSS Animations
- **Date Handling**: date-fns
- **Development**: React Scripts (Create React App)

## 🚀 시작하기

```bash
# 의존성 설치
npm install

# 개발 서버 시작
npm start

# 프로덕션 빌드
npm run build
```

## 🎯 프로젝트 구조

```
nengteol/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── ui/           # UI 컴포넌트
│   │   └── fridge/       # 냉장고 관련 컴포넌트
│   ├── entities/         # 데이터 모델
│   ├── Pages/           # 페이지 컴포넌트
│   ├── utils/           # 유틸리티 함수
│   ├── App.js
│   ├── App.css         # 메인 스타일시트
│   └── index.js
└── package.json
```

## 🎨 디자인 시스템

- **Color Palette**: Cyan-Blue 그라데이션 (#00d4aa → #00a3ff)
- **Typography**: Inter Font Family (300-800)
- **Spacing**: CSS Custom Properties 기반
- **Border Radius**: 12px - 24px 범위
- **Shadows**: Multi-layer 그림자 시스템

## 📱 반응형 디자인

- **Desktop**: 1200px+ (3-column 레이아웃)
- **Tablet**: 768px-1199px (2-column 레이아웃) 
- **Mobile**: ~767px (1-column 레이아웃)

## 🔧 주요 컴포넌트

- **Layout**: Sidebar + Main Content
- **Cards**: Glassmorphism 카드 시스템
- **Buttons**: Premium 버튼 (Primary, Outline)
- **Badges**: 상태별 배지 시스템
- **Tabs**: 고급 탭 네비게이션

---

**🎉 Base44 수준을 넘어서는 Ultra Premium UI 경험을 해보세요!**