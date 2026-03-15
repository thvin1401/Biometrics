$IMAGE_NAME = "opencv-equalizer"

$INPUT = "$PWD/input"
$OUTPUT = "$PWD/output"

Write-Host "=== OpenCV Histogram Equalizer ==="

if (!(Test-Path $INPUT)) {
    Write-Host "Creating input folder..."
    New-Item -ItemType Directory -Path $INPUT | Out-Null
}

if (!(Test-Path $OUTPUT)) {
    Write-Host "Creating output folder..."
    New-Item -ItemType Directory -Path $OUTPUT | Out-Null
}

Write-Host "Building Docker image..."
docker build -t $IMAGE_NAME .

Write-Host "Running container..."

docker run --rm `
-v ${INPUT}:/app/input `
-v ${OUTPUT}:/app/output `
$IMAGE_NAME

Write-Host "Done. Check output folder."