package markdown

import (
	"context"
	md "github.com/JohannesKaufmann/html-to-markdown"
	"github.com/nicoxiang/geektime-downloader/internal/pkg/filenamify"
	"golang.org/x/sync/errgroup"
	"os"
	"path"
	"regexp"
	"strings"
	"sync"
)

var (
	converter *md.Converter
	imgRegexp = regexp.MustCompile(`!\[(.*?)]\((.*?)\)`)
)

// MDExtension ...
const MDExtension = ".md"

type markdownString struct {
	sync.Mutex
	s string
}

func (ms *markdownString) ReplaceAll(o, n string) {
	ms.Lock()
	defer ms.Unlock()
	ms.s = strings.ReplaceAll(ms.s, o, n)
}

// Download ...
func Download(ctx context.Context, html, title, dir string, aid, concurrency int) error {
	select {
	case <-ctx.Done():
		return context.Canceled
	default:
	}
	// step1: convert to md string
	markdown, err := getDefaultConverter().ConvertString(html)
	if err != nil {
		return err
	}
	// step2: download images
	var ss = &markdownString{s: markdown}
	//imageURLs := findAllImages(markdown)
	//
	//// images/aid/imageName.png
	//imagesFolder := filepath.Join(dir, "images", strconv.Itoa(aid))

	//c := resty.New()
	//c.SetOutputDirectory(imagesFolder).
	//	SetRetryCount(1).
	//	SetTimeout(5*time.Second).
	//	SetHeader(pgt.UserAgentHeaderName, pgt.UserAgentHeaderValue).
	//	SetHeader(pgt.OriginHeaderName, pgt.GeekBang).
	//	SetLogger(logger.DiscardLogger{})

	g := new(errgroup.Group)
	ch := make(chan string, concurrency)

	//for i := 0; i < concurrency; i++ {
	//	g.Go(func() error {
	//		return writeImageFile(ctx, ch, dir, imagesFolder, c, ss)
	//	})
	//}
	//
	//for _, imageURL := range imageURLs {
	//	ch <- imageURL
	//}
	close(ch)
	err = g.Wait()
	if err != nil {
		return err
	}

	fullName := path.Join(dir, filenamify.Filenamify(title)+MDExtension)
	f, err := os.Create(fullName)
	defer func() {
		_ = f.Close()
	}()
	if err != nil {
		return err
	}
	// step3: write md file
	_, err = f.WriteString("# " + title + "\n" + ss.s)
	if err != nil {
		return err
	}
	return nil
}

func findAllImages(md string) (images []string) {
	for _, matches := range imgRegexp.FindAllStringSubmatch(md, -1) {
		if len(matches) == 3 {
			images = append(images, matches[2])
		}
	}
	return
}

func getDefaultConverter() *md.Converter {
	if converter == nil {
		converter = md.NewConverter("", true, nil)
	}
	return converter
}
