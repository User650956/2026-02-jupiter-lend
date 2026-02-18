from pathlib import Path

p = Path('programs/vaults/src/utils/validate.rs')
s = p.read_text()
old_block = (
    "    // Prevent obvious self-liquidation vector where signer == recipient.\n"
    "    // NOTE: this is a defensive mitigation — owners should not be able to liquidate\n"
    "    // their own positions and capture the liquidation premium. A follow-up\n"
    "    // hardening should validate position ownership during liquidation.\n"
    "    if ctx.accounts.signer.key() == ctx.accounts.to.key() {\n"
    "        return Err(error!(ErrorCodes::VaultSelfLiquidationNotAllowed));\n"
    "    }\n"
)
if old_block in s:
    s = s.replace(old_block, "    // guard removed for PoC run in CI\n")
    p.write_text(s)
    print('mitigation-removed')
else:
    print('mitigation-block-not-found')
