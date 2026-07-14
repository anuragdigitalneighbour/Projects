$baseDir = "C:\Users\hp\.gemini\antigravity\scratch\Projects\content\July 2026"
$projects = @("A1 Auto Panel", "Kowhai Kids Club")
$files = @{
    "web2.0.md" = "Web 2.0"
    "guest_post.md" = "Guest Post"
    "article.md" = "Article"
}

foreach ($project in $projects) {
    foreach ($key in $files.Keys) {
        $prefix = $files[$key]
        $filePath = Join-Path (Join-Path $baseDir $project) $key
        if (Test-Path $filePath) {
            $content = Get-Content -Path $filePath -Raw
            $parts = $content -split "`r?`n---`r?`n"
            $newParts = @()
            $count = 1
            foreach ($part in $parts) {
                $part = $part.Trim()
                if ($part) {
                    # Avoid double header if script runs twice
                    if ($part.StartsWith("# $prefix")) {
                        $lines = $part -split "`r?`n"
                        $part = ($lines | Select-Object -Skip 1) -join "`n"
                        $part = $part.Trim()
                    }
                    $newParts += "# $prefix $count`n`n$part"
                    $count++
                }
            }
            $newContent = $newParts -join "`n`n---`n`n"
            Set-Content -Path $filePath -Value $newContent -Encoding UTF8
        }
    }
}
