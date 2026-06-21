from IPython.display import HTML, display

APP_HTML = r"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>發票核算助手</title>
  <style>
    :root {
      --bg: #f6f7f8;
      --surface: #ffffff;
      --surface-2: #f0f4f3;
      --ink: #17201d;
      --muted: #63716d;
      --line: #dce4e1;
      --accent: #0f766e;
      --accent-2: #b45309;
      --danger: #b42318;
      --danger-bg: #fff1f0;
      --ok: #16803c;
      --ok-bg: #eef8f1;
      --warn-bg: #fff7e8;
      --shadow: 0 12px 30px rgba(22, 32, 29, 0.08);
      font-family: "Microsoft JhengHei", "PingFang TC", system-ui, sans-serif;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      color: var(--ink);
      background: var(--bg);
    }

    button,
    input,
    select,
    textarea {
      font: inherit;
    }

    button {
      border: 1px solid var(--line);
      background: var(--surface);
      color: var(--ink);
      border-radius: 6px;
      cursor: pointer;
      min-height: 36px;
      transition: background 120ms ease, border-color 120ms ease, transform 120ms ease;
    }

    button:hover {
      background: var(--surface-2);
      border-color: #bfd0cb;
    }

    button:active {
      transform: translateY(1px);
    }

    button.primary {
      border-color: var(--accent);
      background: var(--accent);
      color: white;
    }

    button.primary:hover {
      background: #0c625c;
    }

    button.ghost {
      background: transparent;
    }

    .app-shell {
      min-height: 100vh;
      display: grid;
      grid-template-rows: auto 1fr;
    }

    .topbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
      padding: 14px 18px;
      border-bottom: 1px solid var(--line);
      background: var(--surface);
      position: sticky;
      top: 0;
      z-index: 10;
    }

    .brand {
      display: flex;
      align-items: baseline;
      gap: 12px;
      min-width: 220px;
    }

    .brand h1 {
      margin: 0;
      font-size: 20px;
      letter-spacing: 0;
      white-space: nowrap;
    }

    .period {
      color: var(--muted);
      font-size: 13px;
      white-space: nowrap;
    }

    .top-actions {
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 8px;
      flex-wrap: wrap;
    }

    .workspace {
      display: grid;
      grid-template-columns: minmax(760px, 1fr) 300px;
      gap: 14px;
      padding: 14px;
      min-height: 0;
    }

    .main-panel,
    .side-panel {
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: var(--shadow);
      min-width: 0;
    }

    .main-panel {
      display: grid;
      grid-template-rows: auto auto minmax(0, 1fr) auto;
      overflow: hidden;
    }

    .panel-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 12px;
      border-bottom: 1px solid var(--line);
    }

    .client-fields {
      display: grid;
      grid-template-columns: minmax(150px, 1fr) minmax(130px, 0.8fr) minmax(130px, 0.8fr);
      gap: 8px;
      flex: 1;
    }

    .field {
      display: grid;
      gap: 4px;
    }

    .field label {
      color: var(--muted);
      font-size: 12px;
    }

    input,
    select,
    textarea {
      width: 100%;
      min-height: 34px;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 7px 9px;
      color: var(--ink);
      background: white;
    }

    input:focus,
    select:focus,
    textarea:focus {
      outline: 2px solid rgba(15, 118, 110, 0.18);
      border-color: var(--accent);
    }

    .quick-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      padding: 10px 12px;
      border-bottom: 1px solid var(--line);
      background: #fbfcfc;
    }

    .quick-actions button {
      padding: 0 10px;
    }

    .mode-select {
      display: flex;
      align-items: center;
      gap: 8px;
      min-height: 36px;
      padding: 0 10px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: white;
    }

    .mode-select label {
      color: var(--muted);
      font-size: 13px;
      white-space: nowrap;
    }

    .mode-select select {
      min-height: 28px;
      padding: 4px 24px 4px 4px;
      border: 0;
      background: transparent;
    }

    .paste-box {
      display: none;
      padding: 0 12px 12px;
      background: #fbfcfc;
      border-bottom: 1px solid var(--line);
    }

    .paste-box.open {
      display: grid;
      gap: 8px;
    }

    .paste-box textarea {
      resize: vertical;
      min-height: 96px;
      font-family: Consolas, "Microsoft JhengHei", monospace;
      font-size: 13px;
    }

    .table-wrap {
      min-height: 360px;
      overflow: auto;
      background: white;
    }

    table {
      width: 100%;
      min-width: 1540px;
      border-collapse: separate;
      border-spacing: 0;
      font-size: 13px;
    }

    th,
    td {
      border-right: 1px solid var(--line);
      border-bottom: 1px solid var(--line);
      padding: 0;
      vertical-align: middle;
      background: white;
    }

    th {
      position: sticky;
      top: 0;
      z-index: 2;
      background: #eef4f2;
      color: #26332f;
      font-weight: 700;
      height: 36px;
      text-align: left;
      padding: 0 8px;
      white-space: nowrap;
    }

    td.index {
      width: 42px;
      text-align: center;
      color: var(--muted);
      background: #f8faf9;
    }

    td input,
    td select {
      border: 0;
      border-radius: 0;
      min-height: 36px;
      padding: 6px 8px;
      background: transparent;
    }

    td input.number {
      text-align: right;
      font-variant-numeric: tabular-nums;
    }

    tr.bad td {
      background: var(--danger-bg);
    }

    tr.warn td {
      background: var(--warn-bg);
    }

    tr.ok td.status-cell {
      background: var(--ok-bg);
    }

    .status-pill {
      display: inline-flex;
      align-items: center;
      min-height: 24px;
      max-width: 160px;
      padding: 2px 8px;
      border-radius: 999px;
      font-size: 12px;
      color: var(--muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .status-pill.ok {
      color: var(--ok);
      background: var(--ok-bg);
    }

    .status-pill.bad {
      color: var(--danger);
      background: var(--danger-bg);
    }

    .status-pill.warn {
      color: var(--accent-2);
      background: var(--warn-bg);
    }

    .row-actions {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      padding: 4px;
    }

    .row-actions button {
      min-width: 30px;
      min-height: 28px;
      padding: 0 6px;
      font-size: 12px;
    }

    .summary {
      display: grid;
      grid-template-columns: repeat(7, minmax(120px, 1fr));
      gap: 1px;
      background: var(--line);
      border-top: 1px solid var(--line);
    }

    .metric {
      background: #fbfcfc;
      padding: 10px 12px;
      min-width: 0;
    }

    .metric span {
      display: block;
      color: var(--muted);
      font-size: 12px;
      margin-bottom: 3px;
    }

    .metric strong {
      display: block;
      font-size: 18px;
      font-variant-numeric: tabular-nums;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .metric.danger strong {
      color: var(--danger);
    }

    .side-panel {
      display: block;
      overflow: hidden;
      align-self: start;
    }

    .side-panel[open] {
      display: grid;
      grid-template-rows: auto auto auto minmax(140px, 1fr);
    }

    .side-panel summary {
      display: flex;
      align-items: center;
      justify-content: space-between;
      min-height: 44px;
      padding: 0 12px;
      cursor: pointer;
      font-weight: 700;
      border-bottom: 1px solid transparent;
      user-select: none;
    }

    .side-panel[open] summary {
      border-bottom-color: var(--line);
    }

    .side-panel summary::after {
      content: "+";
      color: var(--accent);
      font-size: 18px;
    }

    .side-panel[open] summary::after {
      content: "-";
    }

    .calc-head {
      padding: 12px;
      border-bottom: 1px solid var(--line);
    }

    .display {
      background: #17201d;
      color: #f6faf8;
      border-radius: 8px;
      padding: 12px;
      min-height: 70px;
      display: grid;
      align-content: end;
      gap: 4px;
      overflow: hidden;
    }

    .expression {
      color: #b6c8c2;
      min-height: 20px;
      font-size: 13px;
      text-align: right;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .result {
      font-size: 24px;
      line-height: 1.1;
      text-align: right;
      font-variant-numeric: tabular-nums;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .tax-tools {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-top: 10px;
    }

    .tax-tools button {
      padding: 0 8px;
    }

    .keypad {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      padding: 12px;
      border-bottom: 1px solid var(--line);
    }

    .keypad button {
      min-height: 38px;
      font-size: 16px;
      font-weight: 700;
    }

    .keypad button.op {
      color: var(--accent);
      background: #edf7f5;
      border-color: #cce4df;
    }

    .keypad button.equal {
      grid-row: span 2;
      min-height: 84px;
      background: var(--accent);
      border-color: var(--accent);
      color: white;
    }

    .keypad button.zero {
      grid-column: span 2;
    }

    .tape {
      display: grid;
      grid-template-rows: auto 1fr;
      min-height: 0;
    }

    .tape-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 12px;
      border-bottom: 1px solid var(--line);
    }

    .tape-head h2 {
      margin: 0;
      font-size: 15px;
    }

    .tape-list {
      overflow: auto;
      padding: 8px 12px 14px;
      background: #fbfcfc;
    }

    .tape-item {
      display: grid;
      gap: 3px;
      padding: 8px 0;
      border-bottom: 1px dashed #ccd8d4;
      font-variant-numeric: tabular-nums;
    }

    .tape-item .time {
      color: var(--muted);
      font-size: 11px;
    }

    .tape-item .line {
      display: flex;
      justify-content: space-between;
      gap: 8px;
      font-size: 13px;
    }

    .tape-item strong {
      white-space: nowrap;
    }

    .empty-state {
      color: var(--muted);
      padding: 18px 0;
      font-size: 13px;
    }

    .toast {
      position: fixed;
      left: 50%;
      bottom: 18px;
      transform: translateX(-50%);
      background: #17201d;
      color: white;
      padding: 10px 14px;
      border-radius: 8px;
      box-shadow: var(--shadow);
      opacity: 0;
      pointer-events: none;
      transition: opacity 160ms ease, transform 160ms ease;
      z-index: 20;
      max-width: min(520px, calc(100vw - 28px));
    }

    .toast.show {
      opacity: 1;
      transform: translateX(-50%) translateY(-3px);
    }

    @media (max-width: 1100px) {
      .workspace {
        grid-template-columns: 1fr;
      }

      .side-panel[open] {
        min-height: 460px;
      }
    }

    @media (max-width: 720px) {
      .topbar,
      .panel-head {
        align-items: stretch;
        flex-direction: column;
      }

      .brand {
        min-width: 0;
      }

      .brand h1 {
        white-space: normal;
      }

      .top-actions {
        justify-content: stretch;
      }

      .top-actions button,
      .quick-actions button {
        flex: 1 1 130px;
      }

      .client-fields {
        grid-template-columns: 1fr;
      }

      .workspace {
        padding: 8px;
      }

      .summary {
        grid-template-columns: 1fr 1fr;
      }

      .result {
        font-size: 26px;
      }
    }
  </style>
</head>
<body>
  <div class="app-shell">
    <header class="topbar">
      <div class="brand">
        <h1>發票核算助手</h1>
        <span class="period" id="todayLabel"></span>
      </div>
      <div class="top-actions">
        <button type="button" id="copyExcelBtn" title="複製成 Excel 可貼上的表格">複製表格</button>
        <button type="button" id="downloadCsvBtn" title="下載 CSV，Excel 可直接開啟">下載 CSV</button>
        <button type="button" class="primary" id="downloadExcelBtn" title="下載 Excel 可開啟的核算檔">下載 Excel</button>
      </div>
    </header>

    <main class="workspace">
      <section class="main-panel" aria-label="發票整理表格">
        <div class="panel-head">
          <div class="client-fields">
            <div class="field">
              <label for="clientName">客戶名稱</label>
              <input id="clientName" value="範例客戶" autocomplete="off">
            </div>
            <div class="field">
              <label for="periodName">報稅期別</label>
              <input id="periodName" value="115年01-02月" autocomplete="off">
            </div>
            <div class="field">
              <label for="buyerId">買方統編</label>
              <input id="buyerId" placeholder="可留空" inputmode="numeric" autocomplete="off">
            </div>
          </div>
          <button type="button" class="primary" id="addRowBtn">新增憑證</button>
        </div>

        <div class="quick-actions">
          <div class="mode-select">
            <label for="defaultCalcMode">新增列</label>
            <select id="defaultCalcMode">
              <option value="gross">總金額自動拆</option>
              <option value="net">銷售額自動算</option>
              <option value="manual">手動核對</option>
            </select>
          </div>
          <button type="button" id="recalcAllBtn" title="依每列計算方式重新核算">全部重算</button>
          <button type="button" id="fillBuyerBtn" title="把上方買方統編套用到空白列">套用買方統編</button>
          <button type="button" id="pasteToggleBtn" title="貼上 Excel 或 CSV 資料">貼上資料</button>
          <button type="button" id="clearRowsBtn" title="清空表格，保留一列">清空表格</button>
        </div>

        <div class="paste-box" id="pasteBox">
          <textarea id="pasteInput" placeholder="可從 Excel 複製後貼上。欄位順序：日期、發票號碼、賣方名稱、賣方統編、買方統編、摘要、總金額、銷售額、稅額、營業稅別、營業稅扣抵、營所稅科目、營所稅認列"></textarea>
          <div class="top-actions">
            <button type="button" class="ghost" id="pasteCancelBtn">取消</button>
            <button type="button" class="primary" id="pasteApplyBtn">匯入貼上資料</button>
          </div>
        </div>

        <div class="table-wrap">
          <table id="invoiceTable">
            <thead>
              <tr>
                <th>#</th>
                <th>日期</th>
                <th>發票號碼</th>
                <th>賣方名稱</th>
                <th>賣方統編</th>
                <th>買方統編</th>
                <th>摘要</th>
                <th>總金額</th>
                <th>銷售額</th>
                <th>稅額</th>
                <th>營業稅別</th>
                <th>營業稅扣抵</th>
                <th>營所稅科目</th>
                <th>營所稅認列</th>
                <th>計算方式</th>
                <th>核對</th>
                <th>動作</th>
              </tr>
            </thead>
            <tbody id="invoiceBody"></tbody>
          </table>
        </div>

        <footer class="summary" aria-label="合計">
          <div class="metric">
            <span>筆數</span>
            <strong id="rowCount">0</strong>
          </div>
          <div class="metric">
            <span>銷售額合計</span>
            <strong id="netTotal">0</strong>
          </div>
          <div class="metric">
            <span>稅額合計</span>
            <strong id="taxTotal">0</strong>
          </div>
          <div class="metric">
            <span>可扣抵營業稅</span>
            <strong id="vatCreditTotal">0</strong>
          </div>
          <div class="metric">
            <span>營所稅認列金額</span>
            <strong id="corpExpenseTotal">0</strong>
          </div>
          <div class="metric">
            <span>總金額合計</span>
            <strong id="grossTotal">0</strong>
          </div>
          <div class="metric" id="diffMetric">
            <span>核對差額</span>
            <strong id="diffTotal">0</strong>
          </div>
        </footer>
      </section>

      <details class="side-panel" aria-label="輔助計算">
        <summary>輔助計算</summary>
        <div class="calc-head">
          <div class="display" aria-live="polite">
            <div class="expression" id="calcExpression"></div>
            <div class="result" id="calcDisplay">0</div>
          </div>
          <div class="tax-tools">
            <button type="button" id="addTaxBtn" title="未稅金額乘以 1.05">未稅加 5%</button>
            <button type="button" id="splitTaxBtn" title="含稅金額反推銷售額與稅額">含稅拆 5%</button>
          </div>
        </div>

        <div class="keypad" id="keypad">
          <button type="button" data-key="C">C</button>
          <button type="button" data-key="back">退</button>
          <button type="button" data-key="%">%</button>
          <button type="button" class="op" data-key="/">÷</button>
          <button type="button" data-key="7">7</button>
          <button type="button" data-key="8">8</button>
          <button type="button" data-key="9">9</button>
          <button type="button" class="op" data-key="*">×</button>
          <button type="button" data-key="4">4</button>
          <button type="button" data-key="5">5</button>
          <button type="button" data-key="6">6</button>
          <button type="button" class="op" data-key="-">−</button>
          <button type="button" data-key="1">1</button>
          <button type="button" data-key="2">2</button>
          <button type="button" data-key="3">3</button>
          <button type="button" class="op" data-key="+">+</button>
          <button type="button" class="zero" data-key="0">0</button>
          <button type="button" data-key=".">.</button>
          <button type="button" class="equal" data-key="=">=</button>
        </div>

        <section class="tape" aria-label="計算紙帶">
          <div class="tape-head">
            <h2>計算紙帶</h2>
            <button type="button" class="ghost" id="clearTapeBtn">清除</button>
          </div>
          <div class="tape-list" id="tapeList">
            <div class="empty-state">還沒有計算紀錄。</div>
          </div>
        </section>
      </details>
    </main>
  </div>

  <div class="toast" id="toast" role="status"></div>

  <script>
    const currency = new Intl.NumberFormat("zh-TW", {
      maximumFractionDigits: 0
    });

    const state = {
      rows: [],
      tape: [],
      calc: {
        display: "0",
        expression: "",
        overwrite: false
      }
    };

    const columns = [
      "date",
      "invoiceNo",
      "sellerName",
      "sellerId",
      "buyerId",
      "memo",
      "gross",
      "net",
      "tax",
      "taxType",
      "deductible",
      "corpCategory",
      "corpRecognition",
      "calcMode",
    ];

    const els = {
      todayLabel: document.getElementById("todayLabel"),
      clientName: document.getElementById("clientName"),
      periodName: document.getElementById("periodName"),
      buyerId: document.getElementById("buyerId"),
      defaultCalcMode: document.getElementById("defaultCalcMode"),
      body: document.getElementById("invoiceBody"),
      rowCount: document.getElementById("rowCount"),
      netTotal: document.getElementById("netTotal"),
      taxTotal: document.getElementById("taxTotal"),
      vatCreditTotal: document.getElementById("vatCreditTotal"),
      corpExpenseTotal: document.getElementById("corpExpenseTotal"),
      grossTotal: document.getElementById("grossTotal"),
      diffTotal: document.getElementById("diffTotal"),
      diffMetric: document.getElementById("diffMetric"),
      pasteBox: document.getElementById("pasteBox"),
      pasteInput: document.getElementById("pasteInput"),
      calcExpression: document.getElementById("calcExpression"),
      calcDisplay: document.getElementById("calcDisplay"),
      keypad: document.getElementById("keypad"),
      tapeList: document.getElementById("tapeList"),
      toast: document.getElementById("toast")
    };

    function makeRow(overrides = {}) {
      const row = {
        id: crypto.randomUUID ? crypto.randomUUID() : String(Date.now() + Math.random()),
        date: overrides.date || "",
        invoiceNo: overrides.invoiceNo || "",
        sellerName: overrides.sellerName || "",
        sellerId: overrides.sellerId || "",
        buyerId: overrides.buyerId || "",
        memo: overrides.memo || "",
        net: cleanNumber(overrides.net),
        tax: cleanNumber(overrides.tax),
        gross: cleanNumber(overrides.gross),
        taxType: overrides.taxType || "應稅",
        deductible: overrides.deductible || "可扣抵",
        corpCategory: overrides.corpCategory || "待分類",
        corpRecognition: overrides.corpRecognition || "待確認",
        calcMode: overrides.calcMode || "gross",
      };
      applyCalculation(row);
      return row;
    }

    function cleanNumber(value) {
      if (value === undefined || value === null) return "";
      const text = String(value).replace(/,/g, "").trim();
      if (!text) return "";
      const parsed = Number(text);
      return Number.isFinite(parsed) ? String(Math.round(parsed)) : "";
    }

    function numberValue(value) {
      const parsed = Number(String(value || "").replace(/,/g, ""));
      return Number.isFinite(parsed) ? parsed : 0;
    }

    function fmt(value) {
      return currency.format(Math.round(value || 0));
    }

    function taxSplitFromGross(gross) {
      const total = Math.round(numberValue(gross));
      const net = Math.round(total / 1.05);
      return {
        net,
        tax: total - net,
        gross: total
      };
    }

    function grossFromNet(net) {
      const base = Math.round(numberValue(net));
      const tax = Math.round(base * 0.05);
      return {
        net: base,
        tax,
        gross: base + tax
      };
    }

    function applyCalculation(row) {
      if (!row || row.calcMode === "manual") return;

      if (row.taxType !== "應稅") {
        if (row.calcMode === "gross" && row.gross !== "") {
          row.net = String(numberValue(row.gross));
          row.tax = "0";
        }
        if (row.calcMode === "net" && row.net !== "") {
          row.tax = "0";
          row.gross = String(numberValue(row.net));
        }
        return;
      }

      if (row.calcMode === "gross" && row.gross !== "") {
        splitRow(row);
      }

      if (row.calcMode === "net" && row.net !== "") {
        grossRow(row);
      }
    }

    function modeLabel(value) {
      if (value === "net") return "銷售額自動算";
      if (value === "manual") return "手動核對";
      return "總金額自動拆";
    }

    function isVatCredit(row) {
      return row.taxType === "應稅" && row.deductible === "可扣抵";
    }

    function vatCreditAmount(row) {
      return isVatCredit(row) ? numberValue(row.tax) : 0;
    }

    function corporateExpenseAmount(row) {
      if (row.corpRecognition !== "可認列") return 0;
      return isVatCredit(row) ? numberValue(row.net) : numberValue(row.gross);
    }

    function getCheck(row) {
      const net = numberValue(row.net);
      const tax = numberValue(row.tax);
      const gross = numberValue(row.gross);
      const hasAmount = row.net !== "" || row.tax !== "" || row.gross !== "";

      if (!hasAmount) {
        return { type: "warn", label: "待輸入", diff: 0 };
      }

      if (row.taxType !== "應稅") {
        const diff = net + tax - gross;
        if (Math.abs(diff) === 0) return { type: "ok", label: "一致", diff };
        return { type: "bad", label: `差 ${fmt(Math.abs(diff))}`, diff };
      }

      const diff = net + tax - gross;
      const expectedTax = Math.round(net * 0.05);
      const taxDiff = tax - expectedTax;

      if (Math.abs(diff) === 0 && Math.abs(taxDiff) <= 1) {
        return { type: "ok", label: "一致", diff };
      }

      if (Math.abs(diff) <= 2 && Math.abs(taxDiff) <= 2) {
        return { type: "warn", label: `四捨五入 ${fmt(Math.abs(diff || taxDiff))}`, diff };
      }

      return { type: "bad", label: `差 ${fmt(Math.abs(diff || taxDiff))}`, diff: diff || taxDiff };
    }

    function renderRows() {
      els.body.innerHTML = "";
      state.rows.forEach((row, index) => {
        const check = getCheck(row);
        const tr = document.createElement("tr");
        tr.dataset.id = row.id;
        tr.className = check.type;
        tr.innerHTML = `
          <td class="index">${index + 1}</td>
          ${cellInput(row, "date", "date")}
          ${cellInput(row, "invoiceNo", "text")}
          ${cellInput(row, "sellerName", "text")}
          ${cellInput(row, "sellerId", "text", "numeric")}
          ${cellInput(row, "buyerId", "text", "numeric")}
          ${cellInput(row, "memo", "text")}
          ${cellInput(row, "gross", "text", "numeric number")}
          ${cellInput(row, "net", "text", "numeric number")}
          ${cellInput(row, "tax", "text", "numeric number")}
          <td>
            <select data-field="taxType" aria-label="營業稅別">
              ${option("應稅", row.taxType)}
              ${option("零稅率", row.taxType)}
              ${option("免稅", row.taxType)}
              ${option("不計稅", row.taxType)}
            </select>
          </td>
          <td>
            <select data-field="deductible" aria-label="營業稅扣抵">
              ${option("可扣抵", row.deductible)}
              ${option("不可扣抵", row.deductible)}
              ${option("待確認", row.deductible)}
            </select>
          </td>
          <td>
            <select data-field="corpCategory" aria-label="營所稅科目">
              ${option("待分類", row.corpCategory)}
              ${option("進貨", row.corpCategory)}
              ${option("辦公用品", row.corpCategory)}
              ${option("旅費", row.corpCategory)}
              ${option("交通費", row.corpCategory)}
              ${option("郵電費", row.corpCategory)}
              ${option("租金支出", row.corpCategory)}
              ${option("水電瓦斯", row.corpCategory)}
              ${option("廣告費", row.corpCategory)}
              ${option("修繕費", row.corpCategory)}
              ${option("交際費", row.corpCategory)}
              ${option("固定資產", row.corpCategory)}
              ${option("其他費用", row.corpCategory)}
            </select>
          </td>
          <td>
            <select data-field="corpRecognition" aria-label="營所稅認列">
              ${option("待確認", row.corpRecognition)}
              ${option("可認列", row.corpRecognition)}
              ${option("限額/待確認", row.corpRecognition)}
              ${option("不可認列", row.corpRecognition)}
            </select>
          </td>
          <td>
            <select data-field="calcMode" aria-label="計算方式">
              ${option("gross", row.calcMode, "總金額自動拆")}
              ${option("net", row.calcMode, "銷售額自動算")}
              ${option("manual", row.calcMode, "手動核對")}
            </select>
          </td>
          <td class="status-cell"><span class="status-pill ${check.type}">${check.label}</span></td>
          <td>
            <div class="row-actions">
              <button type="button" data-action="recalc" title="依此列計算方式重新核算">重算</button>
              <button type="button" data-action="delete" title="刪除此列">刪</button>
            </div>
          </td>
        `;
        els.body.appendChild(tr);
      });
      updateSummary();
    }

    function cellInput(row, field, type, inputmode = "") {
      const classes = inputmode.includes("number") ? "number" : "";
      const mode = inputmode.includes("numeric") ? " inputmode=\"numeric\"" : "";
      return `<td><input class="${classes}" data-field="${field}" type="${type}" value="${escapeHtml(row[field])}"${mode} autocomplete="off"></td>`;
    }

    function option(value, selected, label = value) {
      return `<option value="${value}"${value === selected ? " selected" : ""}>${label}</option>`;
    }

    function escapeHtml(value) {
      return String(value || "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;");
    }

    function updateSummary() {
      const totals = state.rows.reduce((sum, row) => {
        const check = getCheck(row);
        sum.net += numberValue(row.net);
        sum.tax += numberValue(row.tax);
        sum.vatCredit += vatCreditAmount(row);
        sum.corpExpense += corporateExpenseAmount(row);
        sum.gross += numberValue(row.gross);
        sum.diff += check.diff;
        if (row.net || row.tax || row.gross || row.invoiceNo) sum.count += 1;
        return sum;
      }, { count: 0, net: 0, tax: 0, vatCredit: 0, corpExpense: 0, gross: 0, diff: 0 });

      els.rowCount.textContent = String(totals.count);
      els.netTotal.textContent = fmt(totals.net);
      els.taxTotal.textContent = fmt(totals.tax);
      els.vatCreditTotal.textContent = fmt(totals.vatCredit);
      els.corpExpenseTotal.textContent = fmt(totals.corpExpense);
      els.grossTotal.textContent = fmt(totals.gross);
      els.diffTotal.textContent = fmt(totals.diff);
      els.diffMetric.classList.toggle("danger", totals.diff !== 0);
    }

    function updateRow(id, field, value, options = { render: true }) {
      const row = state.rows.find((item) => item.id === id);
      if (!row) return;
      row[field] = ["net", "tax", "gross"].includes(field) ? cleanNumber(value) : value;
      if (["gross", "net", "taxType", "calcMode"].includes(field)) {
        applyCalculation(row);
      }
      if (options.render) renderRows();
      return row;
    }

    function refreshRowVisual(tr, row, skipField = "") {
      syncAmountInputs(tr, row, skipField);
      const check = getCheck(row);
      tr.className = check.type;
      const pill = tr.querySelector(".status-pill");
      if (pill) {
        pill.className = `status-pill ${check.type}`;
        pill.textContent = check.label;
      }
      updateSummary();
    }

    function syncAmountInputs(tr, row, skipField) {
      ["gross", "net", "tax"].forEach((field) => {
        if (field === skipField) return;
        const input = tr.querySelector(`[data-field="${field}"]`);
        if (input && input.value !== row[field]) input.value = row[field];
      });
    }

    function addRow(overrides) {
      state.rows.push(makeRow(overrides));
      renderRows();
    }

    function splitRow(row) {
      if (!row.gross) return;
      const split = taxSplitFromGross(row.gross);
      row.net = String(split.net);
      row.tax = String(split.tax);
      row.gross = String(split.gross);
    }

    function grossRow(row) {
      if (!row.net) return;
      const calc = grossFromNet(row.net);
      row.net = String(calc.net);
      row.tax = String(calc.tax);
      row.gross = String(calc.gross);
    }

    function exportRows() {
      return state.rows.map((row) => {
        const check = getCheck(row);
        return {
          客戶名稱: els.clientName.value,
          報稅期別: els.periodName.value,
          憑證日期: row.date,
          發票號碼: row.invoiceNo,
          賣方名稱: row.sellerName,
          賣方統編: row.sellerId,
          買方統編: row.buyerId,
          摘要: row.memo,
          總金額: row.gross,
          銷售額: row.net,
          稅額: row.tax,
          營業稅別: row.taxType,
          營業稅扣抵: row.deductible,
          可扣抵營業稅: vatCreditAmount(row),
          營所稅科目: row.corpCategory,
          營所稅認列: row.corpRecognition,
          營所稅認列金額: corporateExpenseAmount(row),
          計算方式: modeLabel(row.calcMode),
          核對狀態: check.label,
          差額: check.diff
        };
      });
    }

    function toDelimited(rows, delimiter) {
      const headers = Object.keys(rows[0] || {
        客戶名稱: "",
        報稅期別: "",
        憑證日期: "",
        發票號碼: "",
        賣方名稱: "",
        賣方統編: "",
        買方統編: "",
        摘要: "",
        總金額: "",
        銷售額: "",
        稅額: "",
        營業稅別: "",
        營業稅扣抵: "",
        可扣抵營業稅: "",
        營所稅科目: "",
        營所稅認列: "",
        營所稅認列金額: "",
        計算方式: "",
        核對狀態: "",
        差額: ""
      });
      const lines = [headers.join(delimiter)];
      rows.forEach((row) => {
        lines.push(headers.map((header) => csvCell(row[header], delimiter)).join(delimiter));
      });
      return lines.join("\n");
    }

    function csvCell(value, delimiter) {
      const text = String(value ?? "");
      if (text.includes(delimiter) || text.includes('"') || text.includes("\n")) {
        return `"${text.replaceAll('"', '""')}"`;
      }
      return text;
    }

    function download(filename, content, type) {
      const blob = new Blob([content], { type });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      link.remove();
      URL.revokeObjectURL(url);
    }

    function excelXml(rows) {
      const headers = Object.keys(rows[0] || exportRows()[0] || {});
      const headerCells = headers.map((header) => `<Cell ss:StyleID="header"><Data ss:Type="String">${xml(header)}</Data></Cell>`).join("");
      const dataRows = rows.map((row) => {
        const cells = headers.map((header) => {
          const value = row[header] ?? "";
          const isNumber = ["銷售額", "稅額", "總金額", "可扣抵營業稅", "營所稅認列金額", "差額"].includes(header) && value !== "";
          return `<Cell><Data ss:Type="${isNumber ? "Number" : "String"}">${xml(value)}</Data></Cell>`;
        }).join("");
        return `<Row>${cells}</Row>`;
      }).join("");

      return `<?xml version="1.0" encoding="UTF-8"?>
<?mso-application progid="Excel.Sheet"?>
<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:o="urn:schemas-microsoft-com:office:office"
 xmlns:x="urn:schemas-microsoft-com:office:excel"
 xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet">
 <Styles>
  <Style ss:ID="header"><Font ss:Bold="1"/><Interior ss:Color="#EEF4F2" ss:Pattern="Solid"/></Style>
 </Styles>
 <Worksheet ss:Name="發票核算">
  <Table>
   <Row>${headerCells}</Row>
   ${dataRows}
  </Table>
 </Worksheet>
</Workbook>`;
    }

    function xml(value) {
      return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;");
    }

    async function copyTable() {
      const text = toDelimited(exportRows(), "\t");
      await navigator.clipboard.writeText(text);
      showToast("已複製，可直接貼到 Excel。");
    }

    function parsePasted(text) {
      return text.trim().split(/\r?\n/).filter(Boolean).map((line) => {
        const cells = line.includes("\t") ? line.split("\t") : line.split(",");
        const calcMode = inferPastedMode(cells[6], cells[7], cells[8]);
        return makeRow({
          date: cells[0],
          invoiceNo: cells[1],
          sellerName: cells[2],
          sellerId: cells[3],
          buyerId: cells[4],
          memo: cells[5],
          gross: cells[6],
          net: cells[7],
          tax: cells[8],
          taxType: cells[9] || "應稅",
          deductible: cells[10] || "可扣抵",
          corpCategory: cells[11] || "待分類",
          corpRecognition: cells[12] || "待確認",
          calcMode,
        });
      });
    }

    function inferPastedMode(gross, net, tax) {
      const hasGross = cleanNumber(gross) !== "";
      const hasNet = cleanNumber(net) !== "";
      const hasTax = cleanNumber(tax) !== "";
      if (hasGross && !hasNet && !hasTax) return "gross";
      if (!hasGross && hasNet && !hasTax) return "net";
      return "manual";
    }

    function showToast(message) {
      els.toast.textContent = message;
      els.toast.classList.add("show");
      window.clearTimeout(showToast.timer);
      showToast.timer = window.setTimeout(() => {
        els.toast.classList.remove("show");
      }, 2200);
    }

    function renderCalc() {
      els.calcDisplay.textContent = state.calc.display;
      els.calcExpression.textContent = state.calc.expression;
    }

    function pressCalc(key) {
      const calc = state.calc;
      if (/^\d$/.test(key) || key === ".") {
        if (calc.overwrite || calc.display === "0") {
          calc.display = key === "." ? "0." : key;
          calc.overwrite = false;
        } else if (key !== "." || !calc.display.includes(".")) {
          calc.display += key;
        }
      } else if (["+", "-", "*", "/"].includes(key)) {
        calc.expression = `${calc.display} ${key}`;
        calc.overwrite = true;
      } else if (key === "%") {
        const before = numberValue(calc.display);
        calc.display = compactNumber(before / 100);
        addTape(`${fmt(before)}%`, calc.display);
      } else if (key === "back") {
        calc.display = calc.display.length > 1 ? calc.display.slice(0, -1) : "0";
      } else if (key === "C") {
        calc.display = "0";
        calc.expression = "";
        calc.overwrite = false;
      } else if (key === "=") {
        calculateExpression();
      }
      renderCalc();
    }

    function calculateExpression() {
      const calc = state.calc;
      const parts = calc.expression.split(" ");
      if (parts.length < 2) return;
      const left = numberValue(parts[0]);
      const op = parts[1];
      const right = numberValue(calc.display);
      let result = right;
      if (op === "+") result = left + right;
      if (op === "-") result = left - right;
      if (op === "*") result = left * right;
      if (op === "/") result = right === 0 ? 0 : left / right;
      const expression = `${compactNumber(left)} ${op} ${compactNumber(right)}`;
      calc.display = compactNumber(result);
      calc.expression = "";
      calc.overwrite = true;
      addTape(expression, calc.display);
    }

    function compactNumber(value) {
      const rounded = Math.round((Number(value) + Number.EPSILON) * 100) / 100;
      return String(rounded).replace(/\.0+$/, "");
    }

    function addTape(label, value, extra = "") {
      const time = new Date().toLocaleTimeString("zh-TW", {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit"
      });
      state.tape.unshift({ time, label, value, extra });
      renderTape();
    }

    function renderTape() {
      if (!state.tape.length) {
        els.tapeList.innerHTML = `<div class="empty-state">還沒有計算紀錄。</div>`;
        return;
      }
      els.tapeList.innerHTML = state.tape.map((item) => `
        <div class="tape-item">
          <div class="time">${item.time}</div>
          <div class="line"><span>${escapeHtml(item.label)}</span><strong>${escapeHtml(item.value)}</strong></div>
          ${item.extra ? `<div class="time">${escapeHtml(item.extra)}</div>` : ""}
        </div>
      `).join("");
    }

    function addTaxFromCalculator() {
      const before = numberValue(state.calc.display);
      const result = grossFromNet(before);
      state.calc.display = String(result.gross);
      state.calc.expression = "";
      state.calc.overwrite = true;
      addTape(`未稅 ${fmt(result.net)} + 5%`, fmt(result.gross), `稅額 ${fmt(result.tax)}`);
      renderCalc();
    }

    function splitTaxFromCalculator() {
      const before = numberValue(state.calc.display);
      const result = taxSplitFromGross(before);
      state.calc.display = String(result.net);
      state.calc.expression = "";
      state.calc.overwrite = true;
      addTape(`含稅 ${fmt(result.gross)} 拆 5%`, `未稅 ${fmt(result.net)}`, `稅額 ${fmt(result.tax)}`);
      renderCalc();
    }

    function setupEvents() {
      document.getElementById("addRowBtn").addEventListener("click", () => addRow({
        buyerId: els.buyerId.value,
        calcMode: els.defaultCalcMode.value
      }));

      document.getElementById("recalcAllBtn").addEventListener("click", () => {
        state.rows.forEach(applyCalculation);
        renderRows();
        showToast("已依每列計算方式重新核算。");
      });

      document.getElementById("fillBuyerBtn").addEventListener("click", () => {
        state.rows.forEach((row) => {
          if (!row.buyerId) row.buyerId = els.buyerId.value;
        });
        renderRows();
        showToast("已套用買方統編到空白列。");
      });

      document.getElementById("clearRowsBtn").addEventListener("click", () => {
        state.rows = [makeRow({
          buyerId: els.buyerId.value,
          calcMode: els.defaultCalcMode.value
        })];
        renderRows();
      });

      document.getElementById("pasteToggleBtn").addEventListener("click", () => {
        els.pasteBox.classList.toggle("open");
        if (els.pasteBox.classList.contains("open")) els.pasteInput.focus();
      });

      document.getElementById("pasteCancelBtn").addEventListener("click", () => {
        els.pasteBox.classList.remove("open");
      });

      document.getElementById("pasteApplyBtn").addEventListener("click", () => {
        const rows = parsePasted(els.pasteInput.value);
        if (!rows.length) return;
        state.rows.push(...rows);
        els.pasteInput.value = "";
        els.pasteBox.classList.remove("open");
        renderRows();
        showToast(`已匯入 ${rows.length} 筆資料。`);
      });

      els.body.addEventListener("input", (event) => {
        const control = event.target.closest("[data-field]");
        if (!control) return;
        const tr = control.closest("tr");
        const row = updateRow(tr.dataset.id, control.dataset.field, control.value, { render: false });
        refreshRowVisual(tr, row, control.dataset.field);
      });

      els.body.addEventListener("change", (event) => {
        const control = event.target.closest("select[data-field]");
        if (!control) return;
        const tr = control.closest("tr");
        const row = updateRow(tr.dataset.id, control.dataset.field, control.value, { render: false });
        refreshRowVisual(tr, row);
      });

      els.body.addEventListener("click", (event) => {
        const button = event.target.closest("button[data-action]");
        if (!button) return;
        const tr = button.closest("tr");
        const row = state.rows.find((item) => item.id === tr.dataset.id);
        if (!row) return;

        if (button.dataset.action === "recalc") applyCalculation(row);
        if (button.dataset.action === "delete") {
          state.rows = state.rows.filter((item) => item.id !== row.id);
          if (!state.rows.length) state.rows.push(makeRow({
            calcMode: els.defaultCalcMode.value
          }));
        }
        renderRows();
      });

      document.getElementById("copyExcelBtn").addEventListener("click", () => {
        copyTable().catch(() => showToast("瀏覽器未允許複製，請改用下載。"));
      });

      document.getElementById("downloadCsvBtn").addEventListener("click", () => {
        const csv = "\uFEFF" + toDelimited(exportRows(), ",");
        download("發票核算.csv", csv, "text/csv;charset=utf-8");
      });

      document.getElementById("downloadExcelBtn").addEventListener("click", () => {
        const rows = exportRows();
        download("發票核算.xls", excelXml(rows), "application/vnd.ms-excel;charset=utf-8");
      });

      els.keypad.addEventListener("click", (event) => {
        const button = event.target.closest("button[data-key]");
        if (button) pressCalc(button.dataset.key);
      });

      document.getElementById("addTaxBtn").addEventListener("click", addTaxFromCalculator);
      document.getElementById("splitTaxBtn").addEventListener("click", splitTaxFromCalculator);

      document.getElementById("clearTapeBtn").addEventListener("click", () => {
        state.tape = [];
        renderTape();
      });

      window.addEventListener("keydown", (event) => {
        if (event.target.matches("input, textarea, select")) return;
        const map = { Enter: "=", Escape: "C", Backspace: "back" };
        const key = map[event.key] || event.key;
        if (/^\d$/.test(key) || [".", "+", "-", "*", "/", "%", "=", "C", "back"].includes(key)) {
          event.preventDefault();
          pressCalc(key);
        }
      });
    }

    function boot() {
      els.todayLabel.textContent = new Date().toLocaleDateString("zh-TW", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit"
      });
      state.rows = [
        makeRow({
          date: "2026-06-21",
          invoiceNo: "AB12345678",
          sellerName: "文具行",
          sellerId: "12345678",
          buyerId: "",
          memo: "辦公用品",
          gross: "1050",
          corpCategory: "辦公用品",
          corpRecognition: "可認列"
        }),
        makeRow({
          date: "2026-06-21",
          invoiceNo: "CD23456789",
          sellerName: "資訊服務",
          sellerId: "87654321",
          buyerId: "",
          memo: "軟體訂閱",
          net: "2000",
          tax: "100",
          gross: "2100",
          corpCategory: "其他費用",
          corpRecognition: "可認列"
        })
      ];
      splitRow(state.rows[0]);
      setupEvents();
      renderRows();
      renderCalc();
      renderTape();
    }

    window.invoiceWorkbench = {
      exportRows,
      excelXml,
      toDelimited
    };

    boot();
  </script>
</body>
</html>
"""

display(HTML(APP_HTML))
